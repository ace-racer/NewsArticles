import constants


news_articles_base_url = "https://newsapi.org/v1/articles?source={0}&apiKey={1}"

# See other values here: https://newsapi.org/
new_provider_source = "bbc-news"

# The file location where the HTML output will be written
output_file_location = "/home/anurag/Knowledge/"

# The name of the output file
output_file_name = "news_articles{0}.html"

# News Article details
new_article_details = [["author", constants.span_element], ["title", constants.span_element], ["description", constants.p_element], ["url", constants.hyperlink_element], ["urlToImage", constants.img_element], ["publishedAt", constants.span_element]]

