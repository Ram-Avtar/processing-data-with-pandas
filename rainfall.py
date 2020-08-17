import pandas as pd


data={
    'Month':pd.Series([
        'january','fabruray','march','april','may',
        'june','july','august'
        ,'september','october','november','december'
    ]),'Rainfall':pd.Series([1.65,1.25,1.94,2.75,
    5.75,3.65,5.05,1.50,1.33,0.07,
    0.50,2.30]),
}



df=pd.read_json(r'./rain.json')

print("Our data Frame :")
print(df,"\n")

# adding zeros in  rows with the missing values
# dfzeros=df.fillna(0)
# print("our data with zero values : \n",dfzeros)

# remove rows with the missing values
dfclean=df.dropna(0)
print("our data with dropped values : \n",dfclean)

# create a count of all rows contain in NaNs
count=0
for index, row in df.iterrows():
    if any(row.isnull()):
        count=count+1
print("\n Number of rows with NaNs : "+str(count))

print("\n","Mean :")
print(dfclean.mean())

print("\n","Median :")
print(dfclean.median())

print("\n","Standard Deviation :")
print(dfclean.std())


# print the rainfall and mean for first few months
rainfall=dfclean['Rainfall'][0:3]
print(rainfall,"\n")
print("Mean Rainfall :",rainfall.mean(),"\n")

print("\n Just temperature and rainfall data ")

dfTempRain=(dfclean[['Temperature','Rainfall']])
print(dfTempRain)
print("mean : \n",dfTempRain.mean())


index=dfclean['Month']
dfIndexed=dfclean.set_index(index)


# requires a properly indexed dataframe
print("Find a roww by vvalue \n ",dfIndexed.loc['March'])
