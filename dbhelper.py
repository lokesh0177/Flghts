import mysql.connector

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Lokesh@123',
                database='flights'

            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection Error')


    def fetch_city_names(self):
        city = []
        self.mycursor.execute(
            """
                SELECT DISTINCT(source) FROM flights.flights
                    UNION
                SELECT DISTINCT(destination) FROM flights.flights
            """
        )
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flight(self,source,destination):
        self.mycursor.execute(
            """
                SELECT Airline,Route,Dep_Time,Duration,Price FROM flights WHERE 
                source = '{}' and destination = '{}'
            """.format(source,destination)
        )
        data = self.mycursor.fetchall()
        return  data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
          SELECT Airline,COUNT(*) FROM flights
          GROUP BY Airline
          """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):

            city = []
            frequency = []

            self.mycursor.execute("""
            SELECT Source,COUNT(*) FROM (SELECT Source FROM flights
    							UNION ALL
    							SELECT Destination FROM flights) t
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC
            """)

            data = self.mycursor.fetchall()

            for item in data:
                city.append(item[0])
                frequency.append(item[1])

            return city, frequency

    def daily_frequency(self):

        date = []
        frequency = []

        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM flights
        GROUP BY Date_of_Journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency