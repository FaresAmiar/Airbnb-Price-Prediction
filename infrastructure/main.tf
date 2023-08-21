provider "aws" {
  region = "eu-west-3"
}

# Bucket S3 pour le dataset
resource "aws_s3_bucket" "dataset_bucket" {
  bucket = "mlops-zoomcamp-dataset"
}

# Bucket S3 pour MLflow artifacts
resource "aws_s3_bucket" "mlflow_bucket" {
  bucket = "mlops-zoomcamp-mlflow"
}

# RDS pour PostgreSQL
resource "aws_db_instance" "mlflow_db" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.micro"
  identifier           = "mlflow"
  username             = "mlflow"
  password             = "mlflowmlflow"
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true
}

# EC2 pour exécuter le code
resource "aws_instance" "ml_ops_ec2" {
  ami           = "ami-07e67bd6b5d9fd892"
  instance_type = "t2.micro"
  key_name      = "mlops"

  tags = {
    Name = "MLOps-Zoomcamp"
  }
}

# Outputs
output "ec2_ip" {
  value = aws_instance.ml_ops_ec2.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.mlflow_db.endpoint
}
