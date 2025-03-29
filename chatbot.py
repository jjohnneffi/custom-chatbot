import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    files = [
        # Please ensure that the file is available in local system working direrctory or change the file path.
        client.files.upload(file="chatbot.txt"),
    ]
    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, I have read the information about Panimalar Engineering College from the provided text file. I understand that it is a Christian minority institution affiliated with Anna University and approved by AICTE, located in Chennai, Tamil Nadu. I have information about its programs, campus, infrastructure, research, industry collaborations, placement record, and extracurricular activities.

I am ready to answer your questions about Panimalar Engineering College. Ask me anything!
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""hi"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Hello! How can I help you today? Do you have any questions about Panimalar Engineering College?
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what do you know about pec"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Based on the information I have, here's what I know about Panimalar Engineering College (PEC):

*   **Location:** Chennai, Tamil Nadu
*   **Affiliation & Approval:** Affiliated with Anna University and approved by AICTE.
*   **Type:** Christian minority institution.
*   **Programs Offered:** Undergraduate and Postgraduate programs in Engineering and Management. Specifically mentioned are:
    *   Computer Science
    *   Information Technology
    *   Electronics & Communication
    *   Mechanical
    *   Electrical & Electronics
    *   Civil Engineering
    *   MBA
*   **Campus:** Sprawling 133-acre campus with a serene and eco-friendly environment.
*   **Infrastructure:**
    *   Digital classrooms
    *   Fully equipped laboratories
    *   Extensive library
    *   Advanced research centers
    *   Separate hostels for boys and girls
*   **Research Focus:** Strong emphasis on innovation with research labs in AI, IoT, Robotics, and Data Science.
*   **Industry Collaboration:** MoUs with top companies such as TCS, Infosys, Wipro, Cognizant, Amazon, and HCL.
*   **Placements:** Consistent placement record with over 95% of students securing jobs in reputed MNCs, offering packages up to ₹15 LPA.
*   **Extracurricular Activities:** Encourages extracurricular activities through:
    *   Technical clubs
    *   Cultural fests
    *   Sports competitions
    *   Entrepreneurship cell supporting student startups.
*   **Overall Focus:** Holistic development, technical excellence, and career readiness.
*   **Reputation:** One of the leading institutions in Tamil Nadu, producing skilled professionals.

In summary, Panimalar Engineering College is a well-established institution that focuses on providing a strong technical education with industry connections and a holistic approach to student development.

Do you have any specific questions you'd like me to answer based on this information?
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""just tell within 60 words """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Panimalar Engineering College, Chennai, is a Christian minority institution affiliated with Anna University. It offers undergraduate and postgraduate programs in engineering and management, boasting a 133-acre campus with modern infrastructure and research labs. With strong industry collaborations and a 95% placement record (up to ₹15 LPA), the college emphasizes holistic development and career readiness, making it a leading institution in Tamil Nadu.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what about placement stuff"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Panimalar Engineering College boasts a **strong placement record**, with **over 95% of students securing jobs** in **reputed MNCs**. They offer salary packages **up to ₹15 LPA**. The college's industry collaborations with companies like TCS, Infosys, Wipro, and Amazon likely contribute to this successful placement rate.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what about departments in the college"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Panimalar Engineering College offers programs in the following departments:

*   **Computer Science**
*   **Information Technology**
*   **Electronics & Communication**
*   **Mechanical**
*   **Electrical & Electronics**
*   **Civil Engineering**
*   **MBA (Management)**
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""then any specific details """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Okay, let's delve into some more specific details about the departments and other aspects of Panimalar Engineering College, based on the information I have:

**Regarding Departments:**

*   While I know the departments offered, I don't have specific details about faculty expertise within each department, specific curriculum details, or specialized labs that might be unique to each department.

**Beyond Departments - Specific Details:**

*   **Research Focus:** The college has a strong emphasis on research, particularly in emerging technologies. Specific research labs exist for:
    *   AI (Artificial Intelligence)
    *   IoT (Internet of Things)
    *   Robotics
    *   Data Science

*   **Industry Collaboration Details:** While I know they have MoUs with TCS, Infosys, Wipro, Cognizant, Amazon, and HCL, I don't have specifics on *what* these collaborations entail. These could include things like:
    *   Internship opportunities for students
    *   Joint research projects
    *   Guest lectures from industry professionals
    *   Curriculum input from industry experts

*   **Extracurricular Activities:** The college seems to actively encourage student participation in various activities, fostering holistic development. Besides the general categories, specific examples aren't given.

*   **Infrastructure:** The description mentions \"advanced research centers,\" but it doesn't provide details about the specific equipment or facilities available within those centers. The \"extensive library\" isn't quantified (e.g., number of books, access to digital resources).

*   **Placement Details:** While a high percentage of students are placed, the text doesn't break down placement rates by department or the average salary across all students.

**In Summary:**

I have a good overview of the college's offerings, but lack granular details on specific departmental strengths, the precise nature of industry partnerships, and the specifics of infrastructure and extracurricular activities. To get those details, you'd likely need to consult the college's website or contact them directly.

Do you have any *specific* area you'd like me to try and extrapolate information from, or perhaps rephrase your question? For example, \"Based on the information, what *might* be some advantages of studying Computer Science at PEC?\"
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""may be about the food"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The provided text about Panimalar Engineering College does not contain any specific information about the food served in the hostels or canteen. Therefore, I cannot provide any details on the quality, variety, or type of food available to students.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""based on the review, float over the website """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""I'm sorry, but I can't directly access or \"float over\" the internet to browse Panimalar Engineering College's website. I am a text-based AI and do not have browsing capabilities. I can only work with the information I have already been given.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""ok fine then any interesting fact about the college """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Based on the information I have, the most interesting facts about Panimalar Engineering College are:

*   **Christian Minority Institution with Broad Appeal:** While being a Christian minority institution, it attracts students from diverse backgrounds seeking quality technical education.
*   **Strong Industry Connections for a Relatively Young College:** The college has managed to establish MoUs with major players like TCS, Infosys, Wipro, Amazon, and HCL, which is impressive and provides students with significant opportunities.
*   **High Placement Rate in a Competitive Market:** Consistently placing over 95% of its students is a strong indicator of the quality of education and the effectiveness of its career services. The ₹15 LPA maximum salary also highlights the potential for high-achieving graduates.
*   **Focus on Emerging Technologies:** The presence of dedicated research labs for AI, IoT, Robotics, and Data Science indicates that the college is forward-thinking and preparing students for the future of the industry.
*   **Balance of Academics and Extracurriculars:** The emphasis on technical clubs, cultural events, sports, and entrepreneurship suggests a holistic approach to student development, creating well-rounded graduates.

Essentially, the most interesting aspects of Panimalar Engineering College are its commitment to quality education, its strong industry ties, its focus on emerging technologies, and its dedication to the overall development of its students.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""any added advantage compared to other colleges"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Based on the provided information, here are some potential advantages Panimalar Engineering College *might* offer compared to other similar engineering colleges in Tamil Nadu:

*   **Strong Industry Connections:** The MoUs with TCS, Infosys, Wipro, Cognizant, Amazon, and HCL are a significant advantage. These partnerships can lead to better internship opportunities, projects, and ultimately, placements. *Not all colleges have this level of industry integration.*

*   **Focus on Emerging Technologies:** The dedicated research labs for AI, IoT, Robotics, and Data Science give students interested in these fields a head start. *Many colleges might offer general computer science or electronics programs, but not all will have these specialized labs.*

*   **High Placement Rate:** A consistent placement rate of over 95% is a strong selling point. *While many colleges advertise placement rates, few consistently achieve such a high percentage.* The package up to ₹15 LPA is also competitive.

*   **Holistic Development:** The emphasis on extracurricular activities, technical clubs, and an entrepreneurship cell suggests the college values developing well-rounded individuals. *Some colleges might prioritize academics to the exclusion of other activities.*

*   **Serene Campus:** The 133-acre eco-friendly campus could be appealing to students who prefer a quieter learning environment. *Many engineering colleges are located in more congested urban areas.*

**However, it's important to note that these are potential advantages based *solely* on the provided text. A more thorough comparison would require considering factors such as:**

*   **Faculty expertise:** The quality of faculty is crucial.
*   **Specific curriculum:** Is the curriculum updated and relevant?
*   **Department-specific strengths:** Does a particular department excel in a specific area?
*   **Student-faculty ratio:** A lower ratio can mean more personalized attention.
*   **Alumni network:** A strong alumni network can be valuable for career opportunities.
*   **Fees and scholarships:** Affordability is a key consideration.

**In conclusion:** Panimalar Engineering College *appears* to offer some significant advantages, particularly in industry connections, emerging technologies, and placement rates. However, further research is needed for a complete comparison.
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""then fine that's it for now """),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Alright! I'm glad I could help. Feel free to ask if you have any more questions about Panimalar Engineering College or anything else in the future. Good luck with your research and decision-making!
"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_ONLY_HIGH",  # Block few
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_ONLY_HIGH",  # Block few
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_ONLY_HIGH",  # Block few
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_ONLY_HIGH",  # Block few
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_CIVIC_INTEGRITY",
                threshold="BLOCK_ONLY_HIGH",  # Block few
            ),
        ],
        response_mime_type="text/plain",
    )

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended.")
            break
        
        contents.append(types.Content(
            role="user",
            parts=[types.Part.from_text(text=user_input)],
        ))
        
        response = ""
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
            config=generate_content_config,
        ):
            response += chunk.text
            print(chunk.text, end="")
        
        print("\n")
        
        contents.append(types.Content(
            role="model",
            parts=[types.Part.from_text(text=response)],
        ))

if __name__ == "__main__":
    generate()
