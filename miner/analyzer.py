import pandas as pd


class Analyzer:
    def seperate_by_facilities(self, df: pd.DataFrame):
        facilities_name_set = set()
        for idx, value in df.iterrows():
            facilities_name_set.add(value['facility'])

        by_facility = dict()

        grouped_df = df.groupby(df.facility)

        for facility in facilities_name_set:
            by_facility[facility] = grouped_df.get_group(facility)

        return by_facility
