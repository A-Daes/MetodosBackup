CREATE FUNCTION ranking() RETURN INTEGER AS '
	BEGIN
	SELECT DISTINCT Customer.FirstName AS Name
	FROM Customer
	WHERE Customer.CustomerId = 
		(SELECT CustomerId COUNT(*) as "count"
		FROM Invoice)
		GROUP BY Customer.FirstName
		ORDER BY "count" DESC
	RETURN Name;
	END;
' LANGUAGE 'plpgsql'

CREATE FUNCTION get_country_rankings(pais, rank) RETURN TEXT AS '
	BEGIN
	IF NOT EXISTS (SELECT 1 FROM Customer WHERE Country = $1)
	RETURN "No existe ese Pais";
	BREAK;
	ENDIF;
	IF NOT EXISTS (SELECT 1 FROM ranking() WHERE "count" = $2)
	RETURN "No existe esa posicion";
	BREAK;
	ENDIF;
	SELECT Customer
	FROM ranking()
	WHERE Customer.Country = $1 AND "count" = $2
	END;
' LANGUAGE 'plpgsql'

CREATE FUNCTION trends(year, month)
	RETURN TEXT AS '
	BEGIN
	IF $1 > 2016 or $1 < 2000 or $2 > 12 or $2 < 1
	RETURN "Mes o a;o invalido";
	BREAK;
	ENDIF;
	CREATE TABLE Tendencia(id INTEGER, year INTEGER, month text, cantidad_ventas INTEGER;
	INSERT INTO Tendencia(S1, S2, S3, S4)
	WHERE 
'