
def provide_weather_advisory(temperature):

  if temperature < 0:
    return "It's freezing! Wear a heavy coat."
  if temperature <= 10:
    return "It's cold! Bundle up."
  if temperature <= 20:
    return "It's cool! A light jacket will do."
  return "It's warm! Enjoy the day."

print(provide_weather_advisory(25))
print(provide_weather_advisory(15))  # Output: "It's cool! A light jacket will do."
print(provide_weather_advisory(5))
print(provide_weather_advisory(-3))