# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/04_Create_Acs_Indicators.ipynb (unless otherwise specified).

__all__ = ['getColName', 'getColByName', 'addKey', 'nullIfEqual', 'sumInts', 'age5', 'age18', 'age24', 'age64', 'age65',
           'bahigher', 'carpool', 'drvalone', 'elheat', 'empl', 'fam', 'female', 'femhhs', 'heatgas', 'hisp', 'hh25inc',
           'hh40inc', 'hh60inc', 'hh75inc', 'hhchpov', 'hhm75', 'hhs', 'hsdipl', 'lesshs', 'male', 'mhhi', 'drvalone',
           'novhcl', 'nohhint', 'othercom', 'paa', 'p2more', 'pasi', 'pubtran', 'pwhite', 'sclemp', 'tpop', 'trav14',
           'trav14', 'trav45', 'trav44', 'unempr', 'unempr', 'walked', 'createAcsIndicator']

# Cell

#@title Run This Cell: Misc Function Declarations
# These functions right here are used in the calculations below.
# Finds a column matchings a substring
def getColName  (df, col): return df.columns[df.columns.str.contains(pat = col)][0]
def getColByName (df, col): return df[getColName(df, col)]

# Pulls a column from one dataset into a new dataset.
# This is not a crosswalk. calls getColByName()
def addKey(df, fi, col):
    key = getColName(df, col)
    val = getColByName(df, col)
    fi[key] = val
    return fi
# Return 0 if two specified columns are equal.
def nullIfEqual(df, c1, c2):
    return df.apply(lambda x:
        x[getColName(df, c1)]+x[getColName(df, c2)] if x[getColName(df, c1)]+x[getColName(df, c2)] != 0 else 0, axis=1)
# I'm thinking this doesnt need to be a function..
def sumInts(df): return df.sum(numeric_only=True)

# Cell
#@title Run This Cell: Create age5

#File: age5.py
#Author: Charles Karpati
#Date: 4/16/19
#Section: Bnia
#Email: karpati1@umbc.edu
#Description:
# Uses ACS Table B01001 - SEX BY AGE
# Universe: Total population
# Table Creates: tpop, female, male, age5 age18 age24 age64 age65
#purpose:
#input: #output:

import pandas as pd
import glob
def age5( df, columnsToInclude ):
    fi = pd.DataFrame()
    columns = ['B01001_027E_Total_Female_Under_5_years',
               'B01001_003E_Total_Male_Under_5_years',
               'B01001_001E_Total' , 'tract']
    columns.extend(columnsToInclude)
    for col in columns:
        fi = addKey(df, fi, col)

    fi['final']  = ( df[ 'B01001_003E_Total_Male_Under_5_years' ]
               + df[ 'B01001_027E_Total_Female_Under_5_years' ]
    ) / df['B01001_001E_Total'] * 100

    return fi

# Cell
#@title Run This Cell: age18

#File: age18.py
#Author: Charles Karpati
#Date: 4/16/19
#Section: Bnia
#Email: karpati1@umbc.edu
#Description:
# Uses ACS Table B01001 - SEX BY AGE
# Universe: Total population
# Table Creates: tpop, female, male, age5 age18 age24 age64 age65
#purpose:
#input: #output:

import pandas as pd
import glob
def age18( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = ['B01001_001E_Total',
            'B01001_004E_Total_Male_5_to_9_years',
            'B01001_005E_Total_Male_10_to_14_years' ,
            'B01001_006E_Total_Male_15_to_17_years',
            'B01001_028E_Total_Female_5_to_9_years',
            'B01001_029E_Total_Female_10_to_14_years' ,
             'B01001_030E_Total_Female_15_to_17_years']
  columns = df.filter(regex='001E|004E|005E|006E|028E|029E|030E').columns.values
  columns = numpy.append(columns, columnsToInclude)
  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='004E|005E|006E|028E|029E|030E').sum(axis=1)
) / df['B01001_001E_Total:'] * 100
  return fi

# Cell
#@title Run This Cell: Create age24

#File: age24.py
#Author: Charles Karpati
#Date: 9/8/21
#Section: Bnia
#Email: karpati1@umbc.edu
#Description:
# Uses ACS Table B01001 - SEX BY AGE
# Universe: Total population
# Table Creates: tpop, female, male, age5 age18 age24 age64 age65
#purpose:
#input: #output:

import pandas as pd
import glob
def age24( df, columnsToInclude ):
    fi = pd.DataFrame()
    columns = ['B01001_007E_Total_Male_18_and_19_years',
               'B01001_008E_Total_Male_20_years',
               'B01001_009E_Total_Male_21_years' ,
               'B01001_010E_Total_Male_22_to_24_years' ,
               'B01001_031E_Total_Female_18_and_19_years' ,
               'B01001_032E_Total_Female_20_years' ,
               'B01001_033E_Total_Female_21_years' ,
               'B01001_034E_Total_Female_22_to_24_years',
               'tract']
    columns.extend(columnsToInclude)
    for col in columns:
        fi = addKey(df, fi, col)

    fi['final']  = ( df[ 'B01001_007E_Total_Male_18_and_19_years' ]
               + df[ 'B01001_008E_Total_Male_20_years' ]
               + df[ 'B01001_009E_Total_Male_21_years' ]
               + df[ 'B01001_010E_Total_Male_22_to_24_years' ]
               + df[ 'B01001_031E_Total_Female_18_and_19_years' ]
               + df[ 'B01001_032E_Total_Female_20_years' ]
               + df[ 'B01001_033E_Total_Female_21_years' ]
               + df[ 'B01001_034E_Total_Female_22_to_24_years' ]
    ) / df['B01001_001E_Total'] * 100

    return fi

# Cell
#@title Run This Cell: age64

import pandas as pd
import glob
def age64( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='012E|013E|014E|015E|016E|017E|018E|019E|036E|037E|038E|039E|040E|041E|042E|043E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='012E|013E|014E|015E|016E|017E|018E|019E|036E|037E|038E|039E|040E|041E|042E|043E').sum(axis=1)
) / df['B01001_001E_Total:'] * 100

  return fi

# Cell
#@title Run This Cell: age65

import pandas as pd
import glob
def age65( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|020E|021E|022E|023E|024E|025E|044E|045E|046E|047E|048E|049E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='020E|021E|022E|023E|024E|025E|044E|045E|046E|047E|048E|049E').sum(axis=1)
) / df['B01001_001E_Total:'] * 100

  return fi

# Cell
#@title Run This Cell: bahigher

import pandas as pd
import glob
def bahigher( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='005E|006E|001E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='005E|006E').sum(axis=1)
) / df['B06009_001E'] * 100

  return fi

# Cell
#@title Run This Cell: - carpool

import pandas as pd
import glob
def carpool( df, columnsToInclude ):
  # Final Dataframe
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|017E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_017E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: - drvalone

import pandas as pd
import glob
def drvalone( df, columnsToInclude ):
  # Final Dataframe
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -elheat

import pandas as pd
import glob
def elheat( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='B25040_004E|B25040_001E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B25040_004E').sum(axis=1)
) / ( df.filter(regex='B25040_001E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -empl

import pandas as pd
import glob
def empl( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -fam

import pandas as pd
import glob
def fam( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -female

import pandas as pd
import glob
def female( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['female']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -femhhs

import pandas as pd
import glob
def femhhs( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['femhhs']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -heatgas

import pandas as pd
import glob
def heatgas( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell:  hisp

import pandas as pd
import glob
def hisp( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = ['B03002_001E_Total',
             'B03002_012E_Total_Hispanic_or_Latino']
  columns = df.filter(regex='001E|012E').columns.values
  columns = numpy.append(columns, columnsToInclude)
  for col in columns:
      print('addKey df',df.columns,'fi',fi.columns,'col: ', col)
      fi = addKey(df, fi, col)
      print(' ')

  fi['final']  = ( df.filter(regex='012E').sum(axis=1)
) / df['B03002_001E_Total:'] * 100

  return fi

# Cell
#@title Run This Cell: hh25inc

import pandas as pd
import glob
def hh25inc( df, columnsToInclude ):
  df.columns = df.columns.str.replace(r"[$]", "")
  fi = pd.DataFrame()
  columns = ['B19001_001E_Total',
       "B19001_002E_Total_Less_than_10,000",
       "B19001_003E_Total_10,000_to_14,999",
       "B19001_004E_Total_15,000_to_19,999",
       "B19001_005E_Total_20,000_to_24,999"]
  columns = df.filter(regex='002E|003E|004E|005E|001E').columns.values
  columns = numpy.append(columns, columnsToInclude)
  for col in columns:
      print('addKey col: ', col, df.columns)
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='002E|003E|004E|005E').sum(axis=1)
) / df['B19001_001E_Total:'] * 100

  return fi

# Cell
#@ title Run This Cell: -hh40inc

import pandas as pd
import glob
def hh40inc( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -hh60inc

import pandas as pd
import glob
def hh60inc( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -hh75inc

import pandas as pd
import glob
def hh75inc( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -hhchpov

import pandas as pd
import glob
def hhchpov( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -hhm75

import pandas as pd
import glob
def hhm75( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -hhs

import pandas as pd
import glob
def hhs( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -hsdipl

import pandas as pd
import glob
def hsdipl( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -lesshs

import pandas as pd
import glob
def lesshs( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@ title Run This Cell: -male

import pandas as pd
import glob
def male( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
# @title Run This Cell : Create MHHI

#File: mhhi.py
#Author: Charles Karpati
#Date: 1/24/19
#Section: Bnia
#Email: karpati1@umbc.edu
#Description:
# Uses ACS Table B19001 - HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2016 INFLATION-ADJUSTED DOLLARS)
# Universe: Households
# Table Creates: hh25 hh40 hh60 hh75 hhm75, mhhi
#purpose: Produce Sustainability - Percent of Population that Walks to Work Indicator
#input:
#output:
import pandas as pd
import glob

def mhhi( df, columnsToInclude = [] ):
  info = pd.DataFrame(
      [
          ['B19001_002E', 0, 10000],
          ['B19001_003E', 10000, 4999 ],
          ['B19001_004E', 15000, 4999 ],
          ['B19001_005E', 20000, 4999 ],
          ['B19001_006E', 25000, 4999 ],
          ['B19001_007E', 30000, 4999],
          ['B19001_008E', 35000, 4999 ],
          ['B19001_009E', 40000, 4999 ],
          ['B19001_010E', 45000, 4999 ],
          ['B19001_011E', 50000, 9999 ],
          ['B19001_012E', 60000, 14999],
          ['B19001_013E', 75000, 24999 ],
          ['B19001_014E', 100000, 24999 ],
          ['B19001_015E', 125000, 24999 ],
          ['B19001_016E', 150000, 49000 ],
          ['B19001_017E', 200000, 1000000000000000000000000 ],

      ],
      columns=['variable', 'lower', 'range']
  )

  # Final Dataframe
  data_table = pd.DataFrame()
  for index, row in info.iterrows():
      data_table = addKey(df, data_table, row['variable'])

  # Accumulate totals accross the columns.
  # Midpoint: Divide column index 16 (the last column) of the cumulative totals
  temp_table = data_table.cumsum(axis=1)
  temp_table['midpoint'] = (temp_table.iloc[ : , -1 :] /2) # V3
  temp_table['midpoint_index'] = False
  temp_table['midpoint_index_value'] = False # Z3
  temp_table['midpoint_index_lower'] = False # W3
  temp_table['midpoint_index_range'] = False # X3
  temp_table['midpoint_index_minus_one_cumulative_sum'] = False #Y3
  # step 3 - csa_agg3: get the midpoint index by "when midpoint > agg[1] and midpoint <= agg[2] then 2"

  # Get CSA Midpoint Index using the breakpoints in our info table.
  for index, row in temp_table.iterrows():
      # Get the index of the first column where our midpoint is greater than the columns value.
      midpoint = row['midpoint']
      midpoint_index = 0
      # For each column (except the 6 columns we just created)

      # The tracts midpoint was < than the first tracts value at column 'B19001_002E_Total_Less_than_$10,000'
      if( midpoint < int(row[0]) or row[-6] == False ):
        temp_table.loc[ index, 'midpoint_index' ] = 0
      else:
        for column in row.iloc[:-6]:
            # set midpoint index to the column with the highest value possible that is under midpoint
            if( midpoint >= int(column) ):
                if midpoint==False: print (str(column) + ' - ' + str(midpoint))
                temp_table.loc[ index, 'midpoint_index' ] = midpoint_index +1
            midpoint_index += 1

  # temp_table = temp_table.drop('Unassigned--Jail')
  for index, row in temp_table.iterrows():
    temp_table.loc[ index, 'midpoint_index_value' ] = data_table.loc[ index, data_table.columns[row['midpoint_index']] ]
    temp_table.loc[ index, 'midpoint_index_lower' ] = info.loc[ row['midpoint_index'] ]['lower']
    temp_table.loc[ index, 'midpoint_index_range' ] = info.loc[ row['midpoint_index'] ]['range']
    temp_table.loc[ index, 'midpoint_index_minus_one_cumulative_sum'] = row[ row['midpoint_index']-1 ]

  # This is our denominator, which cant be negative.
  for index, row in temp_table.iterrows():
    if row['midpoint_index_value']==False:
      temp_table.at[index, 'midpoint_index_value']=1;

  #~~~~~~~~~~~~~~~
  # Step 3)
  # Run the Calculation
  # Calculation = (midpoint_lower::numeric + (midpoint_range::numeric * ( (midpoint - midpoint_upto_agg) / nullif(midpoint_total,0)
  # Calculation = W3+X3*((V3-Y3)/Z3)

  # v3 -> 1 - midpoint of households  == sum / 2
  # w3 -> 2 - lower limit of the income range containing the midpoint of the housing total == row[lower]
  # x3 -> width of the interval containing the medium == row[range]
  # z3 -> number of hhs within the interval containing the median == row[total]
  # y3 -> 4 - cumulative frequency up to, but no==NOT including the median interval
  #~~~~~~~~~~~~~~~

  def finalCalc(x):
    return ( x['midpoint_index_lower']+ x['midpoint_index_range']*(
      ( x['midpoint']-x['midpoint_index_minus_one_cumulative_sum'])/ x['midpoint_index_value'] )
    )

  temp_table['final'] = temp_table.apply(lambda x: finalCalc(x), axis=1)

  temp_table[columnsToInclude] = df[columnsToInclude]

  return temp_table

# Cell
#@ title Run This Cell: -nilf

import pandas as pd
import glob
def drvalone( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: novhcl

import pandas as pd
import glob
def novhcl( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = ['B08201_002E_Total_No_vehicle_available','B08201_001E_Total']
  columns = df.filter(regex='002E|003E|004E|005E|001E').columns.values
  columns = numpy.append(columns, columnsToInclude)
  for col in columns:
      print('addKey df',df.columns,'fi',fi.columns,'col: ', col)
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='002E').sum(axis=1)
) / df['B08201_001E_Total:'] * 100

  return fi

# Cell
#@title Run This Cell: nohhint

import pandas as pd
import glob
def nohhint( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = ['B28011_001E_Total',
       'B28011_002E_Total_With_an_Internet_subscription',
       'B28011_003E_Total_With_an_Internet_subscription_Dial-up_alone',
       'B28011_004E_Total_With_an_Internet_subscription_Broadband_such_as_cable,_fiber_optic,_or_DSL',
       'B28011_005E_Total_With_an_Internet_subscription_Satellite_Internet_service',
       'B28011_006E_Total_With_an_Internet_subscription_Other_service',
       'B28011_007E_Total_Internet_access_without_a_subscription',
       'B28011_008E_Total_No_Internet_access']
  columns = df.filter(regex='008E|001E').columns.values
  columns = numpy.append(columns, columnsToInclude)
  for col in columns:
      print('addKey df',df.columns,'col: ', col)
      fi = addKey(df, fi, col)
      print(' ')

  # Calculate
  fi['nohhint']  = ( df.filter(regex='008E').sum(axis=1)
) / df['B28011_001E_Total:'] * 100

  return fi

# Cell
#@ title Run This Cell: -othercom

import pandas as pd
import glob
def othercom( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['othercom']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: paa

import pandas as pd
import glob
def paa( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = ['B03002_001E_Total:',
             'B03002_004E_Total_Not_Hispanic_or_Latino_Black_or_African_American_alone']
  columns = df.filter(regex='001E|004E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      print('addKey df',df.columns,'fi',fi.columns,'col: ', col)
      fi = addKey(df, fi, col)

  fi['paa']  = ( df.filter(regex='004E').sum(axis=1)
) / df['B03002_001E_Total:'] * 100

  return fi

# Cell
#@title Run This Cell: -p2more

import pandas as pd
import glob
def p2more( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='B08101_009E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: -pasi ***

import pandas as pd
import glob
def pasi( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='006E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: -pubtran

import pandas as pd
import glob
def pubtran( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='025E|001E|049E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['pubtran']  = ( df.filter(regex='025E').sum(axis=1)
) / ( df.filter(regex='B08101_001E|B08101_049E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: pwhite

import pandas as pd
import glob
def pwhite( df, columnsToInclude ):

  fi = pd.DataFrame()
  columns = ['B03002_001E_Total',
             'B03002_003E_Total_Not_Hispanic_or_Latino_White_alone']
  columns = df.filter(regex='001E|003E').columns.values
  columns = numpy.append(columns, columnsToInclude)
  for col in columns:
      print('addKey df',df.columns,'fi',fi.columns,'col: ', col)
      fi = addKey(df, fi, col)
      print(' ')

  # Calculate
  fi['pwhite']  = ( df.filter(regex='003E').sum(axis=1)
) / df['B03002_001E_Total:'] * 100

  return fi

# Cell
#@title Run This Cell: -racdiv ***

# Cell
#@title Run This Cell: -sclemp

import pandas as pd
import glob
def sclemp( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E|004E|005E|006E|009E|013E|018E|019E|020E|023E|027E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['sclemp']  = ( df.filter(regex='004E|005E|006E|009E|013E|018E|019E|020E|023E|027E').sum(axis=1)
) / ( df.filter(regex='001E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: -tpop

import pandas as pd
import glob
def tpop( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='001E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['tpop']  = ( df.filter(regex='001E').sum(axis=1)
)

  return fi

# Cell
#@title Run This Cell: trav14

import pandas as pd
import glob
def trav14( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = df.filter(regex='002E|003E|004E|001E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['age65']  = ( df.filter(regex='002E|003E|004E').sum(axis=1)
) / df['B08303_001E'] * 100

  return fi

# Cell
#@title Run This Cell: trav29

import pandas as pd
import glob
def trav14( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = df.filter(regex='005E|006E|007E|001E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['age65']  = ( df.filter(regex='005E|006E|007E').sum(axis=1)
) / df['B08303_001E'] * 100

  return fi

# Cell
#@title Run This Cell: Create trav45

#File: trav45.py
#Author: Charles Karpati
#Date: 1/17/19
#Section: Bnia
#Email: karpati1@umbc.edu
#Description:
# Uses ACS Table B08303 - TRAVEL TIME TO WORK,
# (Universe: Workers 16 years and over who did not work at home)
# Table Creates: trav14, trav29, trav44, trav45
#purpose: Produce Sustainability - Percent of Employed Population with Travel Time to Work of 45 Minutes and Over Indicator
#input:
#output:

import pandas as pd
import glob
def trav45(df, columnsToInclude = [] ):

    # Final Dataframe
    fi = pd.DataFrame()
    columns = ['B08303_011E','B08303_012E','B08303_013E','B08303_001E', 'tract']
    columns.extend(columnsToInclude)
    for col in columns:
        fi = addKey(df, fi, col)

    # Numerators
    numerators = pd.DataFrame()
    columns = ['B08303_011E','B08303_012E','B08303_013E']
    for col in columns:
        numerators = addKey(df, numerators, col)

    # Denominators
    denominators = pd.DataFrame()
    columns = ['B08303_001E']
    for col in columns:
        denominators = addKey(df, denominators, col)
    # construct the denominator, returns 0 iff the other two rows are equal.

    #~~~~~~~~~~~~~~~
    # Step 3)
    # Run the Calculation
# ( (value[1] + value[2] + value[3] ) / nullif(value[4],0) )*100
    #~~~~~~~~~~~~~~~
    fi['numerator'] = numerators.sum(axis=1)
    fi['denominator'] = denominators.sum(axis=1)
    fi = fi[fi['denominator'] != 0] # Delete Rows where the 'denominator' column is 0
    fi['final'] = (fi['numerator'] / fi['denominator'] ) * 100

    return fi

# Cell
#@title Run This Cell: Create trav44

#File: trav44.py
#Author: Charles Karpati
#Date: 1/17/19
#Section: Bnia
#Email: karpati1@umbc.edu
#Description:
# Uses ACS Table B08303 - TRAVEL TIME TO WORK,
# (Universe: Workers 16 years and over who did not work at home)
# Table Creates: trav14, trav29, trav44, trav45
#purpose: Produce Sustainability - Percent of Employed Population with Travel Time to Work of 30-44 Minutes Indicator
#input:
#output:

import pandas as pd
import glob
def trav44( df, columnsToInclude = [] ):

    fi = pd.DataFrame()
    columns = ['B08303_008E','B08303_009E','B08303_010E','B08303_001E', 'tract']
    columns.extend(columnsToInclude)
    for col in columns:
        fi = addKey(df, fi, col)

    # Numerators
    numerators = pd.DataFrame()
    columns = ['B08303_008E','B08303_009E','B08303_010E']
    for col in columns:
        numerators = addKey(df, numerators, col)

    # Denominators
    denominators = pd.DataFrame()
    columns = ['B08303_001E']
    for col in columns:
        denominators = addKey(df, denominators, col)
    # construct the denominator, returns 0 iff the other two rows are equal.

    #~~~~~~~~~~~~~~~
    # Step 3)
    # Run the Calculation
    # ( (value[1] + value[2] + value[3] ) / nullif(value[4],0) )*100
    #~~~~~~~~~~~~~~~
    fi['numerator'] = numerators.sum(axis=1)
    fi['denominator'] = denominators.sum(axis=1)
    fi = fi[fi['denominator'] != 0] # Delete Rows where the 'denominator' column is 0
    fi['final'] = (fi['numerator'] / fi['denominator'] ) * 100

    return fi

# Cell
#@title Run This Cell: -unempl

import pandas as pd
import glob
def unempr( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='003E|010E|017E|024E|031E|038E|045E|052E|059E|066E|089E|096E|103E|110E|117E|124E|131E|138E|145E|152E|008E|015E|022E|029E|036E|043E|050E|057E|064E|071E|094E|101E|108E|115E|122E|129E|136E|143E|150E|157E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['final']  = ( df.filter(regex='008E|015E|022E|029E|036E|043E|050E|057E|064E|071E|094E|101E|108E|115E|122E|129E|136E|143E|150E|157E').sum(axis=1)
) / ( df.filter(regex='003E|010E|017E|024E|031E|038E|045E|052E|059E|066E|089E|096E|103E|110E|117E|124E|131E|138E|145E|152E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: -unempr

import pandas as pd
import glob
def unempr( df, columnsToInclude ):
  fi = pd.DataFrame()

  columns = df.filter(regex='006E|013E|020E|027E|034E|041E|048E|055E|062E|069E|092E|099E|106E|113E|120E|127E|134E|141E|148E|155E|008E|015E|022E|029E|036E|043E|050E|057E|064E|071E|094E|101E|108E|115E|122E|129E|136E|143E|150E|157E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['unempr']  = ( df.filter(regex='008E|015E|022E|029E|036E|043E|050E|057E|064E|071E|094E|101E|108E|115E|122E|129E|136E|143E|150E|157E').sum(axis=1)
) / ( df.filter(regex='006E|013E|020E|027E|034E|041E|048E|055E|062E|069E|092E|099E|106E|113E|120E|127E|134E|141E|148E|155E').sum(axis=1)
) * 100

  return fi

# Cell
#@title Run This Cell: -walked

import pandas as pd
import glob
def walked( df, columnsToInclude ):

  fi = pd.DataFrame()

  columns = df.filter(regex='001E|049E|009E').columns.values
  columns = numpy.append(columns, columnsToInclude)

  for col in columns:
      fi = addKey(df, fi, col)

  fi['walked']  = ( df.filter(regex='033E').sum(axis=1)
) / ( df.filter(regex='001E|049E').sum(axis=1)
) * 100

  return fi

# Cell
# @ title Run This Cell: Create createIndicator()
import geopandas as gpd
import numpy as np
import pandas as pd
from .acsDownload import retrieve_acs_data
from dataplay.merge import mergeDatasets
from dataplay.intaker import Intake
def createAcsIndicator(state, county, tract, year, tableId,
                    mergeUrl, merge_left_col, merge_right_col, merge_how, groupBy,
                    aggMethod, method, columnsToInclude, finalFileName=False):

  # Pull the data
  df = retrieve_acs_data(state, county, tract, tableId, year)
  print('Table: ' + tableId + ', Year: ' + year + ' imported.')

  # Get the crosswalk
  if mergeUrl:
    right_ds = Intake.getData( mergeUrl )
    print( right_ds.columns )
    print('Merge file imported')
    # Merge crosswalk with the data
    df = mergeDatasets( left_ds=df, right_ds=right_ds,
                  left_col=merge_left_col, right_col=merge_right_col,
                  merge_how=merge_how, interactive=False )

    print('Both are now merged.')

  # Group and Aggregate
  if groupBy:
    df = df.groupby(groupBy)
    print('Aggregating...')
    if aggMethod == 'sum':
      df = sumInts(df)
    else:
      df = sumInts(df)
    print('Aggregated')

  # Create the indicator
  print('Creating Indicator')
  resp = method( df, columnsToInclude)
  print('Indicator Created')
  if finalFileName:
    resp.to_csv(finalFileName, quoting=csv.QUOTE_ALL)
    print('Indicator Saved')

  return resp