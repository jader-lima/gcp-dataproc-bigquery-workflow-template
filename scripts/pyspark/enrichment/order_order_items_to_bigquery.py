import argparse
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import sum,avg,max,count,min
from pyspark.sql.functions import from_json, col, expr, to_date



def create_spark_session(app_name):
    spark_packages_list = [
            'io.delta:delta-core_2.12:2.3.0',
            'io.delta:delta-storage:2.3.0',
            'com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.17.1'
        ]

    spark_packages = ",".join(spark_packages_list)
    return SparkSession \
        .builder \
        .appName("File Streaming Demo") \
        .master("local[3]") \
        .config("spark.databricks.delta.schema.autoMerge.enabled", "true")\
        .config("spark.jars.packages", spark_packages) \
        .config("spark.bigquery.project", "tough-victor-415420:") \
        .config("spark.bigquery.tempGcsBucket", "storage_bigdata_001/bigquerytemp") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.databricks.delta.schema.autoMerge.enabled","true") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .enableHiveSupport()\
        .getOrCreate()


def read_delta_file(spark,path:str):
    return spark.read \
            .format('delta') \
            .option('inferSchema', 'true') \
            .load(path)

def write_delta_file(path_bronze:str,df:DataFrame):
    df.write.format('delta').mode('overwrite').save(path_bronze )

def join_dataframes(df1:DataFrame, df2:DataFrame,join_field:str,join_type:str):
    return df1.join(df2,[join_field],join_type).drop(df2[join_field])

def select_fields(df:DataFrame):
    return  df.select('price','freight_value','order_status',\
                       'order_id','order_item_id','customer_id','product_id',\
                                              'seller_id','order_purchase_timestamp',\
                                              'order_delivered_customer_date','order_estimated_delivery_date')

def order_items_report(df:DataFrame):
    return df\
        .groupBy('order_status','order_id','order_item_id','customer_id','product_id'\
        ,'seller_id','order_purchase_timestamp','order_delivered_customer_date','order_estimated_delivery_date') \
        .agg(sum("price").alias("price"),\
            sum("freight_value").alias("freight_value"),
            count("order_item_id").alias("order_items_count"))

def create_date_partition(df:DataFrame):
    return df.withColumn('datePartition',to_date('order_purchase_timestamp'))

def load_to_bigquery(df, bigquery_table:str,temp_bucket:str,datePartition:str):
    df.write.format("bigquery") \
    .option("table", bigquery_table) \
    .option("temporaryGcsBucket",temp_bucket)\
    .option("partitionField", datePartition)\
    .mode("overwrite")\
    .save()

def main(app_name, bronze_orders_zone, bronze_orders_items_zone,bigquery_table,temp_bucket  ):
    spark = create_spark_session(app_name)
    df_orders = read_delta_file(spark, bronze_orders_zone)
    df_order_items = read_delta_file(spark, bronze_orders_items_zone)
    df_join = join_dataframes(df_orders, df_order_items,"order_id","inner")
    df_join_selected = select_fields(df_join)
    df_order_items_report = order_items_report(df_join_selected)
    df_order_items_report = create_date_partition(df_order_items_report)
    datePartition = 'datePartition'
    load_to_bigquery(df_order_items_report, bigquery_table,temp_bucket,datePartition)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--app_name',
        type=str,
        dest='app_name',
        required=True,
        help='Pyspark Application Name')

    parser.add_argument(
        '--bronze_orders_zone',
        type=str,
        dest='bronze_orders_zone',
        required=True,
        help='URI of the GCS transient bucket')

    parser.add_argument(
        '--bronze_orders_items_zone',
        type=str,
        dest='bronze_orders_items_zone',
        required=True,
        help='URI of the GCS bronze bucket')
    
    parser.add_argument(
        '--bigquery_table',
        type=str,
        dest='bigquery_table',
        required=True,
        help='URI of the GCS bronze bucket') 

    parser.add_argument(
        '--temp_bucket',
        type=str,
        dest='temp_bucket',
        required=True,
        help='URI of the GCS bronze bucket')


    known_args, pipeline_args = parser.parse_known_args()
    main(known_args.app_name, known_args.bronze_orders_zone, known_args.bronze_orders_items_zone,known_args.bigquery_table, known_args.temp_bucket)


