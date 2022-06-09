# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/CityFinance_histaxhometaxowntax.ipynb (unless otherwise specified).

__all__ = ['homtax']

# Cell
def homtax(df, totalres, year):
  homtax = df.copy()
  # Aggregate Numeric Values by Sum
  homtax['homtaxCount'] = 1
  homtax = homtax.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included. among other things
  homtax = totalres[ ['CSA2010','totalres'+year] ].merge( homtax, left_on='CSA2010', right_on='CSA2010', how='outer' )

  # Update the baltimore CSA.
  homtax.at[55,'homtaxCount'] = homtax['homtaxCount'].sum()

  # Create the Indicator
  homtax['47-homtax'+year] = homtax['homtaxCount'] * 1000 / totalres['totalres'+year]

  homtax = homtax[['CSA2010', 'homtaxCount', '47-homtax'+year, 'totalres'+year ]]

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Histax/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  prevYear = 'histax'+ str( int(year) - 1 )
  if prevYear in compareYears.columns:
    homtax = homtax.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    homtax['change'] = homtax['47-homtax'+year] - homtax[ prevYear ]
    homtax['percentChange'] = homtax['change'] / homtax[ prevYear ] * 1000
    homtax['change'] = homtax['change'].apply(lambda x: "{:.2f}".format(x) )
    homtax = homtax[['CSA2010', 'homtaxCount', 'totalres19', 'homtax18', '47-homtax19', 'percentChange', 'change']]

  return homtax