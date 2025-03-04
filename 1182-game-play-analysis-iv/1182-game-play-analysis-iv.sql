select round(sum(login)/count(distinct player_id),2) fraction from
(select player_id,datediff(event_date,min(event_date) over (partition by player_id))=1 login from activity) as newtable;