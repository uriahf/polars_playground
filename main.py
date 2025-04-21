import polars as pl

def main():
    print("Hello from polars-playground!")


if __name__ == "__main__":
    main()


trips = pl.read_csv(
"data/202403-citibike-tripdata.csv",
try_parse_dates=True,
schema_overrides={
"start_station_id": pl.String,
"end_station_id": pl.String,
},
).sort(
"started_at"
)

trips.height

print(trips[:, :4])
print(trips[:, 4:8])
print(trips[:, 8:])


print(2+2)