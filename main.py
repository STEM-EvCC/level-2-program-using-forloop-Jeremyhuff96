mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

missions = 0
successfulMissions = 0
missionsBefore2000 = []


for i in range(len(mission_names)):

    missions += 1

    if mission_success[i]:
        successfulMissions += 1

    if mission_years[i] < 2000:

        missionsBefore2000.append(mission_names[i])

    successrate = (successfulMissions/missions) * 100

print (f"Total Missions: {missions}")
print (f"Successful Missions: {successfulMissions}")
print (f"Success Rate: {successrate:.2f}%")
print ("Missions before 2000: " )

for mission in missionsBefore2000:
    print (f"-{mission}")
                   