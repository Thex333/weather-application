import weather_forecast as wf
location=input("Enter Location Here :")
# author : Tushar

print('Displaying weather report for :'+location)

weather=wf.forecast(place=location)

print(weather)