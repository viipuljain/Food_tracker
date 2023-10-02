create table log_data(
	id integer primary key autoincrement,
	entry_Data date not NUll
);
create table food(
	id integer primary key autoincrement,
	name text not NUll,
	protein integer not NUll,
	carbohydrates integer not NUll,
	fat integer not NUll,
	cal integer not Null
);
create table food_date(
	food_id integer not null,
	log_data data not null,
	primary key(food_id,log_data)
);