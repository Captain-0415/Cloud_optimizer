CREATE DATABASE cloud_optimizer;

CREATE TABLE aws_instances(
	Instance_Id VARCHAR(25) PRIMARY KEY,
	Instance_Name text NOT NULL,
	Owner text NOT NULL,
	Purpose text NOT NULL,
	State character varying(20),
	State_transistion_time timestamptz NOT NULL,
	Age integer NOT NULL,
	DND character varying(20),
	YEB character varying(20),
	Instance_Type character varying(20),
	Type_violation character varying(20),
	Architecture character varying(25),
	Image_id character varying(30),
	private_ip character varying(15),
	public_ip character varying(15),
	virtualization_type text,
	vpc_id text,
	Region character varying(25),
	Cost_saved double precision
);

