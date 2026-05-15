select ip, count(*) as acessos
from login_logs
group by ip
order by acessos desc