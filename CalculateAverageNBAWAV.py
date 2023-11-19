import pandas as pd
import glob
import os

def calculate_average_wav():
    path = 'csvFiles/'  # Replace with the correct path
    all_files = glob.glob(path + "*.csv")
    print("Found files:", all_files)

    # Dictionary to store the sum of WAV values per team per season
    season_team_wav_totals = {}

    for filename in all_files:
        team_name = os.path.basename(filename).split('.')[0]  # Extract team name from filename
        df = pd.read_csv(filename)

        for index, row in df.iterrows():
            year = row.get('Year')
            wav = row.get('VORP')

            # Only process non-NaN and numeric values
            if year is not None and pd.notna(wav):
                if year not in season_team_wav_totals:
                    season_team_wav_totals[year] = {}
                if team_name not in season_team_wav_totals[year]:
                    season_team_wav_totals[year][team_name] = 0
                season_team_wav_totals[year][team_name] += wav

    # Calculate the average of team totals per season and round it
    average_wav_per_season = {year: round(sum(team_totals.values()) / len(team_totals))
                              for year, team_totals in season_team_wav_totals.items() if team_totals}

    print("Average WAV per season:", average_wav_per_season)

    df_average_wav = pd.DataFrame(list(average_wav_per_season.items()), columns=['Year', 'Average wAV'])
    df_average_wav.to_csv('average_wav_per_season.csv', index=False)

calculate_average_wav()
