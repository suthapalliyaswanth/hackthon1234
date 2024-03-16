from django.http import HttpResponse
from django.shortcuts import render
# forms.py
from django import forms
from django.contrib.auth.decorators import login_required

from services.models import DiabetesPrediction, FoodPrediction, HeartDiseasePrediction, SleepCyclePrediction
from . import heart_disease, sleep_prediction, training  # Import your sleep cycle logic module


def handlesleep(request):
    if request.method == 'POST':
        form = SleepCycle(request.POST)
        if form.is_valid():
            # Process the form data
            start = form.cleaned_data['Start']
            end = form.cleaned_data['End']
            regularity = form.cleaned_data['Regularity']
            steps = form.cleaned_data['Steps']
            movements_per_hour = form.cleaned_data['Movements_per_hour']
            time_in_bed_seconds = form.cleaned_data['Time_in_bed_seconds']
            time_asleep_seconds = form.cleaned_data['Time_asleep_seconds']
            time_before_sleep_seconds = form.cleaned_data['Time_before_sleep_seconds']
            window_start = form.cleaned_data['Window_start']
            window_stop = form.cleaned_data['Window_stop']
            snore_time = form.cleaned_data['Snore_time']

            # Perform sleep cycle prediction logic here
            prediction = sleep_prediction.main(start, end, regularity, steps, movements_per_hour,
                                                                time_in_bed_seconds, time_asleep_seconds,
                                                                time_before_sleep_seconds, window_start,
                                                                window_stop, snore_time)
            SleepCyclePrediction.objects.create(user=request.user, start=start, end=end, regularity=regularity, steps=steps, movements_per_hour=movements_per_hour, time_in_bed_seconds=time_in_bed_seconds, time_asleep_seconds=time_asleep_seconds, time_before_sleep_seconds=time_before_sleep_seconds, window_start=window_start, window_stop=window_stop, snore_time=snore_time, result=prediction)
            # Render a template with the prediction result or redirect to another page
            return HttpResponse(f"Quality of sleep {prediction[0]}%")
    else:
        form = SleepCycle()

    return render(request, 'sleep_cycle_form.html', {'form': form})
class DiabetesPredictionForm(forms.Form):
    Pregnancies = forms.FloatField(label='Pregnancies')
    Glucose = forms.FloatField(label='Glucose')
    BloodPressure = forms.FloatField(label='Blood Pressure')
    SkinThickness = forms.FloatField(label='Skin Thickness')
    Insulin = forms.FloatField(label='Insulin')
    BMI = forms.FloatField(label='BMI')
    DiabetesPedigreeFunction = forms.FloatField(label='Diabetes Pedigree Function')
    Age = forms.FloatField(label='Age')
    
def diabetes_prediction(request):
    if request.method == 'POST':
        form = DiabetesPredictionForm(request.POST)
        if form.is_valid():
            # Process the form data
            pregnancies = form.cleaned_data['Pregnancies']
            glucose = form.cleaned_data['Glucose']
            blood_pressure = form.cleaned_data['BloodPressure']
            skin_thickness = form.cleaned_data['SkinThickness']
            insulin = form.cleaned_data['Insulin']
            bmi = form.cleaned_data['BMI']
            diabetes_pedigree_function = form.cleaned_data['DiabetesPedigreeFunction']
            age = form.cleaned_data['Age']
            inputs = [pregnancies, glucose, blood_pressure, skin_thickness,
                                                                    insulin, bmi, diabetes_pedigree_function, age]
            # Perform diabetes prediction logic here
            prediction = training.predict(*inputs)
            DiabetesPrediction.objects.create(user=request.user, pregnancies = pregnancies, glucose=glucose, blood_pressure=blood_pressure, skin_thickness=skin_thickness, insulin=insulin, bmi=bmi, diabetes_pedigree_function=diabetes_pedigree_function, age=age, result=prediction)

            # Render a template with the prediction result or redirect to another page
            return HttpResponse(f'{prediction[0]} {'' if not prediction[1] else prediction[1]}')
    else:
        form = DiabetesPredictionForm()

    return render(request, 'diabetes_prediction_form.html', {'form': form})
class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[('male', 'Male'), ('female', 'Female')])
    chestpain = forms.ChoiceField(label='Chest Pain', choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Anginal Pain'), (4, 'Asymptomatic')])
    blood_pressure = forms.IntegerField(label='Blood Pressure')
    cholesterol = forms.IntegerField(label='Cholesterol')
    fasting_blood_sugar = forms.ChoiceField(label='Fasting Blood Sugar', choices=[(0, 'Lower than 120mg/dl'), (1, 'Greater than 120mg/dl')])
    ekg_results = forms.ChoiceField(label='ekg_results', choices=[(0, 'No Disease'), (1, 'Has Disease')])
    max_heart_rate = forms.IntegerField(label='Max Heart Rate')
    exercise_induced_angina = forms.ChoiceField(label='Exercise Induced Angina', choices=[(0, 'No'), (1, 'Yes')])
    st_depression = forms.FloatField(label='ST Depression')
    st_slope = forms.ChoiceField(label='Slope of ST', choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Downsloping')])
    num_vessels = forms.IntegerField(label='Number of Vessels Fluro')
    thallium = forms.ChoiceField(label='Thallium', choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversable Defect')])


class SleepCycle(forms.Form):
    Start = forms.FloatField(label='Start')
    End = forms.FloatField(label='End')
    Regularity = forms.FloatField(label='Regularity')
    Steps = forms.FloatField(label='Steps')
    Movements_per_hour = forms.FloatField(label='Movements per hour')
    Time_in_bed_seconds = forms.FloatField(label='Time in bed (seconds)')
    Time_asleep_seconds = forms.FloatField(label='Time asleep (seconds)')
    Time_before_sleep_seconds = forms.FloatField(label='Time before sleep (seconds)')
    Window_start = forms.FloatField(label='Window start')
    Window_stop = forms.FloatField(label='Window stop')
    Snore_time = forms.FloatField(label='Snore time')
    

def heart_disease_prediction(request):
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            # Process the form data
            age = form.cleaned_data['age']
            sex = 1 if form.cleaned_data['sex'] == 'male' else 0 
            chestpain = form.cleaned_data['chestpain']
            blood_pressure = form.cleaned_data['blood_pressure']
            cholesterol = form.cleaned_data['cholesterol']
            fasting_blood_sugar = form.cleaned_data['fasting_blood_sugar']
            ekg_results = form.cleaned_data['ekg_results']
            max_heart_rate = form.cleaned_data['max_heart_rate']
            exercise_induced_angina = form.cleaned_data['exercise_induced_angina']
            st_depression = form.cleaned_data['st_depression']
            st_slope = form.cleaned_data['st_slope']
            num_vessels = form.cleaned_data['num_vessels']
            thallium = form.cleaned_data['thallium']
            
            # Perform prediction logic here
            prediction = heart_disease.main(age, sex, chestpain, blood_pressure, cholesterol, fasting_blood_sugar, ekg_results, max_heart_rate, exercise_induced_angina, st_depression, st_slope, num_vessels, thallium)
            
            # Create HeartDiseasePrediction object
            if request.user.is_authenticated:
                HeartDiseasePrediction.objects.create(user=request.user, **form.cleaned_data, result=prediction)
            else:
                # Handle unauthenticated user (optional)
                pass

            # Render a template with the prediction result or redirect to another page
            return HttpResponse(prediction)
    else:
        form = HeartDiseaseForm()
    
    return render(request, 'heart_disease_form.html', {'form': form})

class Food(forms.Form):
    foods = forms.CharField(label="Enter the food items you've consumed ")
texts = {
    'diabeties': '''Diabetes is a chronic condition characterized by high levels of blood glucose (sugar) due to either insufficient insulin production or ineffective insulin utilization by the body. It affects millions of people worldwide and can lead to serious health complications if not properly managed. 
Our platform offers a revolutionary approach to diabetes prevention through predictive modeling. Using a user-friendly interface, individuals can input relevant health data such as age, weight, height, family history of diabetes, physical activity level, and dietary habits. Our sophisticated predictive models analyze this data to assess the risk of developing diabetes, providing personalized insights and actionable recommendations for prevention.''',
    'sleep-cycle': '''Sleep quality plays a vital role in overall health and well-being, impacting cognitive function, mood, immune function, and physical health. However, factors such as stress, lifestyle habits, and medical conditions can affect sleep quality, leading to sleep disturbances and related health issues.
Our innovative project focuses on predicting sleep quality based on user inputs and lifestyle factors. Through a user-friendly interface, individuals can input relevant data such as bedtime habits, sleep duration, sleep environment, stress levels, and daytime activities.''',
    'heart': '''Heart diseases encompass a range of conditions that affect the heart and blood vessels, often leading to serious health complications. As one of the leading causes of mortality worldwide, understanding the risk factors, symptoms, and preventive measures for heart diseases is crucial for maintaining heart health.

Through a user-friendly interface, individuals can input relevant health data such as age, gender, blood pressure, cholesterol levels, and lifestyle factors. Our sophisticated predictive models analyze this data to assess the risk of various heart conditions, including coronary artery disease, heart failure, arrhythmias, and valvular heart disease. By harnessing the power of data-driven insights, our platform enables early detection and intervention, ultimately leading to better outcomes and improved quality of life for our users. Join us in revolutionizing preventive healthcare and taking proactive steps towards a healthier heart.''',
    'dietary-plan': '''Maintaining a healthy diet is essential for overall well-being and disease prevention. However, with the abundance of dietary information available, finding the right approach for your individual needs can be overwhelming. Our personalized diet suggestion model aims to simplify this process by analyzing your unique health profile and lifestyle factors to provide tailored dietary recommendations.
sing our user-friendly interface, you can input relevant health information such as age, gender, weight, height, activity level, dietary preferences, and any existing health conditions.'''
}
# Create your views here.
def service_views(request, service: str):
    if service in ['diabeties', 'sleep-cycle', 'heart', 'dietary-plan', 'dietcheck_result']:
        if service == 'sleep-cycle':
            form_a = SleepCycle
            sub = 'handlesleep'
            
            if request.user.is_authenticated:
                hist = SleepCyclePrediction.objects.filter(user=request.user)
                field_names = [field.name for field in SleepCyclePrediction._meta.get_fields()]
            else:
                hist= None
                field_names = None
        elif service == 'heart':
            form_a = HeartDiseaseForm
            sub = 'heart_disease_prediction'
            if request.user.is_authenticated:
                hist = HeartDiseasePrediction.objects.filter(user=request.user)
                field_names = [field.name for field in HeartDiseasePrediction._meta.get_fields()]
            else:
                hist= None
                field_names = None
        elif service == 'diabeties':
            form_a = DiabetesPredictionForm
            sub = 'diabetes_prediction'
            if request.user.is_authenticated:
                hist = DiabetesPrediction.objects.filter(user= request.user)
                field_names = [field.name for field in DiabetesPrediction._meta.get_fields()]
            else:
                hist= None
                field_names = None
        elif service == 'dietary-plan':
            form_a = Food
            sub = 'dietcheck_result'
            if request.user.is_authenticated:
                hist = FoodPrediction.objects.filter(user=request.user)
                field_names = [field.name for field in FoodPrediction._meta.get_fields()]
            else:
                hist= None
                field_names = None
        elif service == 'dietcheck_result':
            return dietcheck_result(request)
        # print(service)
        print(hist)
        return render(request, 'service.html', {'service': service.title().replace('-', ' '),'form': form_a, 'text': texts[service], 'sub': sub, 'hist': hist, 'field_names': field_names})
    else:
        return HttpResponse('404 Not Found')

# views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# import pickle
# import pandas as pd

# def index(request):
#     return render(request, 'index.html')

# def healthblueprint(request):
#     return render(request, 'healthblueprint.html')

# def organhealth(request):
#     return render(request, 'organhealth.html')

# def lungs(request):
#     return render(request, 'lungs.html')

# def heart(request):
#     return render(request, 'heart.html')

# def kidney(request):
#     return render(request, 'kidney.html')

# def liver(request):
#     return render(request, 'liver.html')

# def fooddiet(request):
#     return render(request, 'fooddiet.html')

# def contacts(request):
#     return render(request, 'contacts.html')

# # def diabetes_prediction(request):
# #     if request.method == 'POST':
# #         # Your code for diabetes prediction
# #         return render(request, 'diabetes_result.html', context)
# #     else:
# #         return render(request, 'diabetes_form.html')

# def heart_prediction(request):
#     if request.method == 'POST':
        
#         # Your code for heart disease prediction
#         return render(request, 'heart_result.html', context)
#     else:
#         return render(request, 'heart_form.html')

# def predict_parkinsons(request):
#     if request.method == 'POST':
#         # Your code for Parkinson's disease prediction
#         return render(request, 'parkinsons_result.html', context)
#     else:
#         return render(request, 'parkinsons_form.html')

HEALTHY_FOODS = {"apple", "banana", "spinach", "quinoa", "chicken", "salmon", "avocado", "broccoli", "carrot", "kale",
                 "sweet potato", "brown rice", "eggs", "nuts", "Greek yogurt", "blueberries", "oats", "lean beef",
                 "turkey", "tuna",
                 "asparagus", "bell peppers", "cabbage", "cauliflower", "mushrooms", "green beans", "lentils",
                 "chickpeas", "whole grain bread", "flaxseeds", "chia seeds", "almonds", "walnuts", "pistachios",
                 "coconut oil", "olive oil", "chia seeds",
                 "seaweed", "low-fat dairy products", "watermelon", "kiwi", "oranges", "grapefruit", "pomegranate",
                 "figs", "dates", "prunes", "black beans", "kidney beans", "edamame", "tofu", "tempeh", "brown rice",
                 "wild rice", "basmati rice",
                 "idli", "dosa", "upma", "poha", "dhokla", "carrots", "lettuce", "tomatoes", "celery", "cucumber",
                 "bell peppers", "onions", "garlic", "ginger", "turmeric", "whole wheat bread", "whole grain pasta",
                 "quinoa", "millet", "barley", "beans", "legumes", "chickpeas", "lentils", "peas", "tofu",
                 "sunflower seeds", "pumpkin seeds", "chia seeds", "flaxseeds", "sesame seeds", "walnuts", "almonds",
                 "cashews", "peanuts", "pecans", "pistachios", "hazelnuts", "coconut", "olive oil", "avocado oil",
                 "canola oil", "walnut oil", "sunflower oil",
                 "cooking spray", "vinegar", "balsamic vinegar", "red wine vinegar", "apple cider vinegar", "mustard",
                 "hummus", "salsa", "guacamole", "pesto", "soy sauce", "tamari", "coconut aminos", "herbs", "spices",
                 "turmeric", "cinnamon", "oregano", "basil",
                 "rosemary", "thyme", "sage", "parsley", "cumin", "coriander", "nutritional yeast", "green tea",
                 "black tea", "herbal tea", "coffee", "red wine", "dark chocolate", "cocoa powder",
                 "unsweetened almond milk", "unsweetened coconut milk", "unsweetened soy milk",
                 "unsweetened oat milk", "sparkling water", "mineral water", "still water", "unsweetened herbal tea"}

UNHEALTHY_FOODS = {"cake", "pizza", "burger", "soda", "ice cream", "fries", "chips", "cookies", "candy", "white bread",
                   "processed meats", "fried foods", "white rice", "pastries", "energy drinks", "donuts", "bacon",
                   "hot dogs", "cheeseburgers",
                   "deep-fried foods", "potato chips", "microwave popcorn", "canned soups", "sugary cereals",
                   "artificial sweeteners", "instant noodles", "bottled salad dressings", "margarine", "frozen dinners",
                   "canned fruits in syrup",
                   "store-bought smoothies", "refined pasta", "sweetened yogurt", "high-sugar coffee drinks",
                   "deli meats", "whipped cream", "highly processed snack bars", "store-bought juices", "fast food",
                   "packaged baked goods", "pre-packaged meals",
                   "white rice", "vada", "samosa", "pakora", "bhaji", "bhature", "frozen pizza", "microwave dinners",
                   "potato chips", "tortilla chips", "cheese puffs", "corn chips", "pork rinds", "candy bars",
                   "doughnuts", "pastries", "croissants", "muffins", "white bread", "bagels", "sugary cereals",
                   "pop tarts", "pancakes",
                   "waffles", "syrups", "jellies", "sweetened jams", "processed meats", "hot dogs", "bacon", "sausages",
                   "salami", "pepperoni", "jerky", "instant noodles", "ramen", "cup noodles", "bottled smoothies",
                   "sweetened beverages", "energy drinks", "sugary sodas",
                   "fruit juices", "sports drinks", "sweetened coffee drinks", "sweetened teas", "flavored waters",
                   "milkshakes", "margaritas", "cocktails", "beer", "liquor", "fried chicken", "fried fish",
                   "fried shrimp", "fried calamari", "fried tofu", "fried vegetables",
                   "fried rice", "fried noodles", "fried dumplings", "fried snacks", "fried desserts",
                   "fried ice cream", "fried bananas", "fried dough", "fried candy bars", "fried pastries",
                   "fried cookies", "fried doughnuts", "fried cakes", "fried pies", "fried bread"}


def check_diet(food_choices):
    healthy_count = sum(1 for food in food_choices if food in HEALTHY_FOODS)
    unhealthy_count = sum(1 for food in food_choices if food in UNHEALTHY_FOODS)
    if healthy_count > unhealthy_count:
        return "Good job! You're consuming a healthy diet."
    elif healthy_count < unhealthy_count:
        return "You should consider including more healthy foods in your diet."
    else:
        return "Your diet seems balanced, but you can still improve it by adding more variety."


    
def dietcheck_result(request):
    if request.method == 'POST':
        print(request)
        form = Food(request.POST)
        if form.is_valid():
        # Your code for diet check result
            foods = form.cleaned_data['foods'].split(',')
            result = check_diet(foods)
            FoodPrediction.objects.create(user=request.user, foods=foods, result=result)
            return render(request, 'dietcheck_result.html', {'diet_status': result})
    else:
        return render(request, 'dietcheck_from.html')

# def get_calories(request):
#     if request.method == 'POST':
#         # Your code to get calories
#         return HttpResponse(response)
#     else:
#         return render(request, 'calories.html')

# def exercise(request):
#     return render(request, 'exercise.html')

# def cancer(request):
#     return render(request, 'cancer.html')

# def Kidneycancer(request):
#     return render(request, 'Kidneycancer.html')

# def breastcancer(request):
#     return render(request, 'breastcancer.html')

# def lungcancer(request):
#     return render(request, 'lungcancer.html')

# def carcinomacancer(request):
#     return render(request, 'carcinomacancer.html')

# def melanoma(request):
#     return render(request, 'melanoma.html')

# def lymphomacancer(request):
#     return render(request, 'lymphomacancer.html')

# def leukemiacancer(request):
#     return render(request, 'leukemiacancer.html')

# def bloodcancer(request):
#     return render(request, 'bloodcancer.html')

# def braincancer(request):
#     return render(request, 'braincancer.html')

# def milkdonor(request):
#     return render(request, 'milkdonor.html')

# def prediction(request):
#     return render(request, 'prediction.html')

# def graph(request):
#     return render(request, 'graph.html')

# def heartgraph(request):
#     return render(request, 'heartgraph.html')

# def kidneygraph(request):
#     return render(request, 'kidneygraph.html')

# def livergraph(request):
#     return render(request, 'livergraph.html')

# def lungsgraph(request):
#     return render(request, 'lungsgraph.html')
