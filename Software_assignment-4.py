class Flight:
    def __init__(self, match_location, team01, team02, timing):
        self.match_location = match_location
        self.team01 = team01
        self.team02 = team02
        self.timing = timing
        
class FlightTable:
    def __init__(self, matches):
        self.matches = matches

    def search_match_of_team(self, team):
        result = []
        for match in self.matches:
            if match.team01 == team or match.team02 == team:
                result.append(match)
        return result

    def search_match_of_location(self, location):
        result = []
        for match in self.matches:
            if match.match_location == location:
                result.append(match)
        return result

    def search_match_on_timing(self, time):
        result = []
        for match in self.matches:
            if match.timing == time:
                result.append(match)
        return result
    
matches = [Flight('Mumbai',"India","Sri Lanka","DAY"),
           Flight('Delhi',"England","Australia","DAY-NIGHT"),
           Flight('Chennai',"India","South Africa","DAY"),
           Flight('Indore',"England","Sri Lanka","DAY-NIGHT"),
           Flight('Mohali',"Australia","South Africa","DAY-NIGHT"),
           Flight('Delhi',"India","Australia","DAY"),
           ]

match_table = FlightTable(matches)

print("Please choose the kind of search you want to perform")
print("1. Search for matches of a team")
print("2. Search for matches on a location")
print("3. Search for matches based on timing")
print("4. exit\n")

user_ch = 1
while user_ch != 4:
    user_ch = int(input("Enter your choice: "))
    count = 1
    print()
    if user_ch == 1:
        team = input("Enter the team: ")
        result = match_table.search_match_of_team(team)
    elif user_ch == 2:
        location = input("Enter the location: ")
        result = match_table.search_match_of_location(location)
    elif user_ch == 3:
        timing = input("Enter the timing: ")
        result = match_table.search_match_on_timing(timing)
    elif user_ch == 4:
        print("Exiting...")
        break
    else:
        print("Invalid user_ch")
        result = []
    for match in result:
        print(count,". ",match.match_location, match.team01, match.team02, match.timing)
        count+=1
    print()