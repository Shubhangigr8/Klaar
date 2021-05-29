
$env:PGPASSWORD = 'password';

psql -h '127.0.0.1' -U 'postgres' -d "bankapp" --command "\COPY api_branches(ifsc,bank_id,branch,address,city,district,state,bank_name) from 'branches.csv' WITH(FORMAT csv, HEADER true, encoding 'UTF8')"