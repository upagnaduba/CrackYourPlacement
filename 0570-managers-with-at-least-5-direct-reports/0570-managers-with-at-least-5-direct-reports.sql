select m.name from Employee e
inner join Employee m
on e.managerid=m.id
group by e.managerId
having count(e.managerId)>=5