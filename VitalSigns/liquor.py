# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/City_Liquor_Board_Permits.ipynb (unless otherwise specified).

__all__ = ['liquor', 'fin']

# Cell
def liquor(df, csa, yr):

  # Create the Numerator
  liquor = df.copy()

  liquor = liquor[
    ( liquor['License'].str.contains('LA|LA-2|LAS|LBD7|WA|WAS', regex=True) )
  ]

  liquor['count'] = 1
  liquor = liquor.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  liquor = csa.merge( liquor, left_on='CSA2010', right_on='CSA2010', how='outer' )
  liquor.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  # Baltimoire has records not in the
  liquor.at[55,'count']=liquor['count'].sum()
  # Perform the calculation
  liquor['109-liquor'+year] = liquor['count'] / liquor['tpop10'] * 1000

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Liquor/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  prevYear = 'liquor'+ str( int(year) - 1 )
  if prevYear in compareYears.columns:
    liquor = liquor.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    liquor['change'] = liquor['109-liquor'+year] - liquor[ prevYear ]
    liquor['percentChange'] = liquor['change' ] / liquor[ prevYear ] * 100
    liquor['change'] = liquor['change'].apply(lambda x: "{:.2f}".format(x) )
  print( 'Records Matching Query: ', liquor.size / len(liquor.columns) )
  return liquor

fin = liquor(liquordf, csa, year)
fin.to_csv('109-liquor'+year+'.csv', index=False)
fin.head(60)