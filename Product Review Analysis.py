#Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average".
#  We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]
    #So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."
keywords = ["good", "excellent", "bad", "poor", "average"]

def capitalize_keywords(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())

    return review

# Process each review
for review in reviews:
    updated_review = capitalize_keywords(review, keywords)
    print(updated_review)



#Task 2: Sentiment Tally

#Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.

reviews = [
       "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

positive_words = ["good","impressed", "excellent","highly", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible","average", "horrible", "awful", "disappointing", "subpar"]
positive_total = 0
negative_total = 0
for review in reviews:
    
    for positive_word in positive_words:
        positive_word_count = review.lower().count(positive_word)
        positive_total += positive_word_count
    
    for negative_word in negative_words:
        negative_word_count = review.lower().count(negative_word)
        negative_total += negative_word_count
print (f"The positive word count is",positive_total)
print (f"The negative word count is", negative_total)    

#Task 3: Review Summary



#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

#Example: "This product is really good. I'm...",

reviews = [
       "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

def summarize_reviews(reviews):
  # We want to return an array because the original argument was an array 
  reviews_to_return = [] 

# Iterate through reviews 
  for review in reviews:

    # If the review is less than 30 characters, add the original review to our reviews_to_return 
    if len(review) <= 30:
      reviews_to_return.append(review)

    # If the reviews are longer than 30 characters, we want to do something to it 
    else:
      # Find the cutoff (where is the last space in our first 30 characters?)
      # string.rfind(value we want to find)
      cutoff = review[:30].rfind(' ')

      # review[:cutoff] + ... 
      if cutoff != -1:
        reviews_to_return.append(review[:cutoff] + "...")
      else:
        reviews_to_return.append(review[:30] + "...")

  return reviews_to_return
        


print(summarize_reviews(reviews))