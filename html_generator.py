#Jeff's work from Stage 02 Work Session 5
#I have no idea if this is what you want us to submit, or if you wanted something different. This was working in the testing environment in the course.

# This is the "generate_concept_HTML" function from work_session(s) 4 & 5. 
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text






def make_HTML(concept):
    title = concept[0]
    description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
#EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
#                             ['For Loop', 'For Loops allow you to iterate over lists'],
#                             ['Lists', 'Lists are sequences of data'] ]
#




def make_HTML_for_many_concepts(list_of_concepts):
    place_holder = ""
    for item in list_of_concepts:
        my_HTML_container = make_HTML(item)
        place_holder = place_holder + my_HTML_container
    return place_holder





print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
# The previous line of code should print the following
"""
<div class="concept">
     <div class="concept-title">
         Python
     </div>
    <div class="concept-description">
        Python is a Programming Language
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        For Loop
    </div>
    <div class="concept-description">
        For Loops allow you to iterate over lists
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        Lists
    </div>
    <div class="concept-description">
        Lists are sequences of data
    </div>
</div>
"""
