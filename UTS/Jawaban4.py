#NestedLoop
island = [
  'Kalimantan', 'Sumatra', 'Sulawesi'
]
for region in island:
  WindDirection = [
    'West', 'North', 'South'
  ]
  while WindDirection:
    print(region , WindDirection.pop(0))