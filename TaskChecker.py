import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

class my_dictionary(dict):
  # __init__ function
  def __init__(self):
    self = dict()
  # Function to add key:value
  def add(self, key, value):
    self[key] = value



course_titles = [
    "Soft Skills Training Courses", "Interpersonal Communication Training Courses", 
    "Corporate Communication Training Courses", "Personal Development Training Courses", 
    "Customer Service Training Courses", "Train the Trainer Courses", 
    "Presentation Skills Training Courses", "Public Speaking Training Courses", 
    "OKR Training Courses", "Project Management Training Courses", 
    "Interpersonal Skills Training Courses", "Administrative Personal Assistant Training Courses", 
    "Emotional Intelligence Training Courses", "Technical Writing Training Courses", 
    "Negotiation Skills Training Courses", "Human Resource Management Training Courses", 
    "Sales Training Courses", "Mindfulness Training Courses", 
    "Change Management Training Courses", "Event Management Training Courses", 
    "Diversity and Inclusion Training Courses", "Facilitation Skills Training Courses", 
    "Stakeholder Management Training Courses", "Digital Marketing Training Courses", 
    "Records Management Training Courses", "Strategic Thinking Training Courses", 
    "Adobe Photoshop Training Courses", "Adobe Illustrator Training Courses", 
    "Microsoft Excel Training Courses", "Wordpress Training Courses", 
    "Management Training Courses", "Employee Motivation Training Courses", 
    "NLP Training Courses"
]



def get_33links_from_site(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find all anchor tags with href attributes
        all_links = {a['href'] for a in soup.find_all('a', href=True)}

        # Filter links that contain any of the course titles
        filtered_links = set()
        for link in all_links:
            for title in course_titles:
                if title.lower().replace(' ', '-') in link.lower():
                    filtered_links.add(link)
                    break

        return list(filtered_links)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    



def get_30_links_from_site(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    excluded_links = {
        "https://knowlesti.sg/corporate-team-building-team-bonding-activities-in-singapore/",
        "https://knowlesti.sg/corporate-team-building-team-bonding-activities-in-singapore/",
        "https://knowlesti.sg/live-virtual-training-talks-in-singapore/",
        "https://knowlesti.sg/corporate-training-courses-in-singapore/",
        "https://knowlesti.sg/knowles-training-institute-reviews/",
        "https://knowlesti.sg/business-writing-skills-training/",
        "https://knowlesti.sg/anger-management-training-course-in-singapore/",
        "https://knowlesti.sg/being-assertive-training-course-in-singapore/",
        "https://knowlesti.sg/change-management-skills-training-course-in-singapore/",
        "https://knowlesti.sg/creative-thinking-skills-training-course-in-singapore/",
        "https://knowlesti.sg/emotional-intelligence-training-course-in-singapore/",
        "https://knowlesti.sg/public-speaking-skill-training-course-in-singapore/",
        "https://knowlesti.sg/train-the-trainer-training-course-in-singapore/",
        "https://knowlesti.sg/technical-writing-training-course-in-singapore/",
        "https://knowlesti.sg/talent-management-training-course-in-singapore/",
        "https://knowlesti.sg/stress-management-training-course-in-singapore/",
        "https://knowlesti.sg/strategic-thinking-skills-training-course-in-singapore/",
        "https://knowlesti.sg/creative-problem-solving-skills-training-course-in-singapore/"
        "https://knowlesti.sg/time-management-course-in-singapore/",
        "https://knowlesti.sg/time-management-course-in-singapore",
        "https://knowlesti.sg/creative-problem-solving-skills-training-course-in-singapore"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')

        # Find all <li> tags containing anchor tags with href attributes containing "in-singapore"
        singapore_links = []
        for li in soup.find_all('li'):
            a_tag = li.find('a', href=True)
            if a_tag and "in-singapore" in a_tag['href'].lower() and a_tag['href'] not in excluded_links:
                singapore_links.append(a_tag['href'])

                # Stop fetching more links once we have 30
                if len(singapore_links) >= 30:
                    break

        return singapore_links

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []

def check_links_properties(urls):
    results = []

    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful
            content = response.text

            soup = BeautifulSoup(content, 'html.parser')

            # Check if the page contains "USD"
            has_usd = "USD" in content

            # Check if the page has footers
            has_footer = bool(soup.find('footer'))

            # Check if the page has a section with exactly 12 bullets for course objectives
            course_objectives_section = soup.find('div', class_='course-objectives')
            if course_objectives_section:
                bullets = course_objectives_section.find_all('li')
                has_12_bullets = len(bullets) == 12
            else:
                has_12_bullets = False

            # Prepare the result for the current URL
            result = {
                'URL': url,
                'Has USD': has_usd,
                'Has Footer': has_footer,
                'Has 12 Bullets in Course Objectives': has_12_bullets
            }
            results.append(result)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching {url}: {e}")

    return results

#-------------------------------------------------------------------------------------------------------------------------

# Example usage
urls = [
    "https://knowlesti.sg/"
]
urls2 = [
]
urls3 = [
]

urls_lessthan30 = my_dictionary()

#Prints all the 33 main courses
for url in urls:
    links = get_33links_from_site(url)
    print(f"URL: {url}")
    print("Filtered Links (matching course titles):")
    for link in links:
        urls2.append(link)
       
    print(urls2)
    print()
    print(f"Number of unique links found: {len(links)}")


#Gets all the 30 sub courses
get_30_links_from_site(urls2)
for url in urls2:
    print()
    links = get_30_links_from_site(url)
    print(f"URL: {url}")
    print("SubCourse Links:")
    for link in links:
        print(link)
        urls3.append(link)

    print()
    print(f"Number of links found: {len(links)}")
    if len(links) < 30:
        urls_lessthan30.add(url, len(links))
    print()
    

print("Amount of Subcourses Done",len(urls3))
print("Main Courses less than 30:")
for key, value in urls_lessthan30.items():
    print(str(key) + ': ' + str(value))

# Function call to check properties
results = check_links_properties(urls3)

# Print results
print("Subcourse properties: ")
for result in results:
    print(f"URL: {result['URL']}")
    print(f"Has USD: {result['Has USD']}")
    print(f"Has Footer: {result['Has Footer']}")
    print(f"Has 12 Bullets in Course Objectives: {result['Has 12 Bullets in Course Objectives']}")
    print()