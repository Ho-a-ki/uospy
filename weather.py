
from source import daily, weekly


print('Daily Forecast : ', daily.forecast())
print('Weekly Forecast:')

for i, o in enumerate(weekly.forecast(), 1):
    print( i, o)