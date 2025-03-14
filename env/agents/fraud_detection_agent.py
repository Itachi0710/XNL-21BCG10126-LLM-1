from neo4j import GraphDatabase

class FraudDetectionAgent:
    def __init__(self, uri, user, pwd):
        self._uri = uri
        self._user = user
        self._pwd = pwd
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._pwd))

    def detect_fraud(self, transaction_data):
        with self._driver.session() as session:
            result = session.run("MATCH (a:Transaction) WHERE a.amount > 1000000 RETURN a")
            for record in result:
                print(record)
