from database.DB_connect import DBConnect
from model.drivers import Driver


class DAO():

    @staticmethod
    def getYearSeasons():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct year as y from seasons s   """

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["y"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPilotiAnnoTraguardo(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  select distinct d.*
                    from results res, drivers d, races rac
                    where res.driverId = d.driverId
                    and res.position is not null 
                    and res.raceId = rac.raceId
                    and rac.`year` = %s  """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Driver(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNumVittorie(u: Driver, v: Driver, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """  select count(*) as peso
                    from results res, races rac , results res2, races rac2
                    where res.position is not null 
                    and res.raceId = rac.raceId
                    and rac.`year` = %s

                    and res2.position is not null 
                    and res2.raceId = rac2.raceId
                    and rac2.`year` = %s

                    and res.raceId = res2.raceId	

                    and res.driverId = %s	#il pilota a
                    and res2.driverId = %s	#il pilota b
                    and res.position < res2.position

                    order by res2.raceId  
                                         """

        cursor.execute(query, (anno, anno, u.driverId, v.driverId))

        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        conn.close()
        return result
