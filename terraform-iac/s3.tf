resource "aws_s3_bucket" "this" {
        bucket_prefix = "mvws9-cruz-o"
        force_destroy = true

    tags = {
            Name = "multiverse"
    }
}

resource "aws_s3_bucket_acl" "this" {
    bucket = aws_s3_bucket.this.id
    acl = "private"
}

resource "aws_s3_object" "this" {
    bucket = aws_s3_bucket.this.id
    key = "results.csv"
    source = "${path.module}/results.csv"
    etag = filemd5("${path.module}/results.csv")
}

# Zip the code
#data "archive_file" "source" {
#  type        = "zip"
#  source_dir  = "../python-survey-app"
#  output_path = "../code.zip"
#}

#upload the code
#resource "aws_s3_object" "code" {
#    bucket = aws_s3_bucket.this.id
#    key = "code.zip"
#    source = "${data.archive_file.source.output_path}" # its mean it depended on zip
#    etag = filemd5("${data.archive_file.source.output_path}")
#}

