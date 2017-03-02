from bs4 import BeautifulSoup
import urllib.request
import re

with open("hofstra.csv", "w", encoding="utf-8") as f:
    f.write('institute' + ',' + 'category' + ',' + 'course_num' + ',' + 'course_name' + ',' +
            'credit' + ',' + 'semester' + ',' + 'description' + "\n")

    for i in range(80, 81):
        for j in range(213664, 250000):
            i = str(i)
            j = str(j)

            # i = str(80)
            # j = str(213780)
            url = 'https://bulletin.hofstra.edu/preview_course_nopop.php?catoid=' + i + '&coid=' + j
            # print(url)
            try:
                page = urllib.request.urlopen(url).read()
                # print(page)
                soup = BeautifulSoup(page, 'html.parser')
                institute = 'bulletin.hofstra.edu'


                title = soup.find_all('h1')[1].get_text()
                # print(title)
                t = re.search('(.*)\s(.*)(\s-\s)(.*)', title)
                if t:
                    category = t.group(1)
                    course_num = t.group(1) + t.group(2)
                    course_name = t.group(4)
                else:
                    pass
                # print(category)
                # print(course_num)
                # print(course_name)
                if soup.find_all('strong'):
                    credit = soup.find_all('strong')[1].get_text()
                else:
                    pass
                # print(credit)
                if soup.find_all('hr')[8]:
                    content = soup.find_all('hr')[8].get_text()
                    desc = content[:-345]

                    if re.match(r"Fall, Spring", content):
                        semester = 'Fall&Spring'
                        desc = desc[13:]
                    elif re.match(r"Fall", content):
                        semester = 'Fall'
                        desc = desc[6:]
                    elif re.match(r"Spring", content):
                        semester = 'Spring'
                        desc = desc[7:]
                    else:
                        semester = ''
                    # print(semester)
                    desc = desc.strip().replace('\n', '')
                    # print(desc.strip().replace(',', ';'))
                else:
                    pass

                f.write(institute + ',' + category + ',' + course_num + ',' + course_name.strip().replace(',', ';') + ',' +
                        credit + ',' + semester + ',' + desc.strip().replace(',', ';') + "\n")
            except:
                pass
