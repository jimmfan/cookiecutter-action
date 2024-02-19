from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum
from yaml import safe_load


def apply_transformations(df, transformations):
    for transformation in transformations:
        if "filter" in transformation:
            df = df.filter(transformation["filter"])
        elif "aggregate" in transformation:
            operations = transformation["aggregate"]["operations"]
            agg_exprs = [
                sum(op["sum"]).alias("sum_" + op["sum"])
                if "sum" in op
                else (
                    count(op["count"]).alias("count_" + op["count"])
                    if "count" in op
                    else ""
                )
                for op in operations
            ]
            for op in transformation["aggregate"]["operations"]:
                if "sum" in op:
                    agg_exprs.append(sum(op["sum"]).alias("sum_" + op["sum"]))
                elif "count" in op:
                    agg_exprs.append(count(op["count"]).alias("count_" + op["count"]))
            df = df.groupBy(transformation["aggregate"]["group_by"]).agg(*agg_exprs)
    return df


def main(config):
    spark = SparkSession.builder.appName("YAMLConfiguredPipeline").getOrCreate()

    for table in config["tables"]:
        if "joins" in table:
            # Assuming the first table is the one we're reading and joining
            df_main = spark.read.table(table["name"]).select(table["columns"])

            for join in table["joins"]:
                df_join = spark.read.table(join["join_table"])
                join_condition = [
                    col(key) == col(value)
                    for key, value in join["join_condition"].items()
                ]
                df_main = df_main.join(df_join, on=join_condition, how="inner")

            # Apply transformations
            if "transformations" in table:
                df_main = apply_transformations(df_main, table["transformations"])

            # Assuming the transformation result is to be written to a destination table
            df_main.write.mode("overwrite").saveAsTable("destination_table")


if __name__ == "__main__":
    main(config)
