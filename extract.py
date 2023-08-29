import urllib.request
import json

def main():
    url = input("Please enter the URL of the JSON data: ")
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)
        
        comment_counts = [item['count'] for item in data['comments']]
        total_sum = sum(comment_counts)
        
        print("Comment counts:", comment_counts)
        print("Sum of comment counts:", total_sum)
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
