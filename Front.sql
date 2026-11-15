select ID,count(*) as Duplicate_id from Filtered_data group by Id HAVING count(*)>1  ;

SELECT *
FROM Filtered_data
WHERE ID IN (1012, 1037, 1088, 1105, 1150, 1209)
ORDER BY ID;

select * from Filtered_Data order by ID ;
