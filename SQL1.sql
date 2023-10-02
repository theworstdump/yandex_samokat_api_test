SELECT c.login, 
	   COUNT(o."courierId") 
FROM "Couriers" AS c 
INNER JOIN "Orders" AS o ON c.id = o."courierId" 
WHERE o."inDelivery" = true 
GROUP BY c.id;