# -*- coding: utf-8 -*-


# -- ==combine_team_games(df,== --
joined = pd.merge(df, df, suffixes=['_Home', '_Away'],
                  on=['SEASON_ID', 'GAME_ID', 'GAME_DATE'])
# Filter out any row that is joined to itself.
result = joined[joined.TEAM_ID_Home != joined.TEAM_ID_Away]
# Take action based on the keep_method flag.
if keep_method is None:
    # Return all the rows.
    pass
elif keep_method.lower() == 'home':
    # Keep rows where TEAM_A is the home team.
    result = result[result.MATCHUP_Home.str.contains(' vs. ')]
elif keep_method.lower() == 'away':
    # Keep rows where TEAM_A is the away team.
    result = result[result.MATCHUP_A.str.contains(' @ ')]
elif keep_method.lower() == 'winner':
    result = result[result.WL_A == 'W']
elif keep_method.lower() == 'loser':
    result = result[result.WL_A == 'L']
else:
    raise ValueError(f'Invalid keep_method: {keep_method}')
return result

# -- ==combine_team_games(df,== --