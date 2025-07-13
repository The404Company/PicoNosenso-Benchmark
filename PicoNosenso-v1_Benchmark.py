from transformers import GPT2LMHeadModel, AutoTokenizer
import time
import numpy as np

# Initialize model and tokenizer
model_name = "Lominub44/PicoNosenso-v1"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

trivia_benchmark = [
    ("What is the capital of France?", ["Paris"]),
    ("Who developed the theory of relativity?", ["Einstein"]),
    ("What is the largest mammal on Earth?", ["blue whale"]),
    ("Which element has the chemical symbol 'Au'?", ["gold"]),
    ("How many planets are in our solar system?", ["8", "eight"]),
    ("What is the main component of the Sun?", ["hydrogen"]),
    ("Who painted the Mona Lisa?", ["da Vinci", "Leonardo"]),
    ("What is the hardest natural substance on Earth?", ["diamond"]),
    ("Which ocean is the largest?", ["Pacific"]),
    ("What is the currency of Japan?", ["yen"]),
    ("What is the name of the longest river in Africa?", ["Nile"]),
    ("Who wrote 'the Iliad' and 'the Odyssey'?", ["Homer"]),
    ("What is the largest organ in the human body?", ["skin"]),
    ("Which planet is known as the Red Planet?", ["Mars"]),
    ("What is the boiling point of water at sea level?", ["100?C", "212?F"]),
    ("Who is known as the father of computers?", ["Babbage"]),
    ("What is the tallest mountain in the world?", ["Everest"]),
    ("Which animal is called the King of the Jungle?", ["lion"]),
    ("What is the largest desert on Earth?", ["Antarctica"]),
    ("Who discovered penicillin?", ["Fleming"]),
    ("What is the smallest prime number?", ["2"]),
    ("Which country gifted the Statue of Liberty to the US?", ["France"]),
    ("What is the chemical formula for table salt?", ["NaCl"]),
    ("Who painted 'The Starry Night'?", ["van Gogh"]),
    ("What is the speed of light in a vacuum?", ["299,792 km/s", "186,282 mps"]),
    ("Which language has the most native speakers?", ["Mandarin"]),
    ("What is the main ingredient in guacamole?", ["avocado"]),
    ("Who wrote 'the Theory of Evolution'?", ["Darwin"]),
    ("What is the largest type of big cat?", ["tiger"]),
    ("Which planet has the Great Red Spot?", ["Jupiter"]),
    ("What is the capital of Australia?", ["Canberra"]),
    ("Who was the first woman to win a Nobel Prize?", ["Curie"]),
    ("What is the largest bone in the human body?", ["femur"]),
    ("Which country is known as the Land of the Rising Sun?", ["Japan"]),
    ("What is the study of fossils called?", ["paleontology"]),
    ("Who invented the telephone?", ["Bell"]),
    ("What is the currency of the United Kingdom?", ["pound"]),
    ("Which element is essential for nuclear reactors?", ["uranium"]),
    ("What is the deepest part of the ocean?", ["Mariana Trench"]),
    ("Who is the Greek god of the sea?", ["Poseidon"]),
	("Which planet has the most moons?", ["Saturn"]),
    ("What is the largest internal organ in humans?", ["liver"]),
    ("Who wrote 'Romeo and Juliet'?", ["Shakespeare"]),
    ("What is the largest bird in the world?", ["ostrich"]),
    ("Which country has the most pyramids?", ["Sudan"]),
    ("What is the only mammal capable of true flight?", ["bat"]),
    ("Who discovered gravity?", ["Newton"]),
    ("What is the largest reef system?", ["Great Barrier Reef"]),
    ("Which country invented tea?", ["China"]),
    ("What is the world's most venomous fish?", ["stonefish"]),
    ("Who founded Microsoft?", ["Gates"]),
    ("What is the smallest country by area?", ["Vatican"]),
    ("Which animal has the longest lifespan?", ["quahog", "ocean quahog"]),
    ("What is the capital of Brazil?", ["Brasilia"]),
    ("Who painted the ceiling of the Sistine Chapel?", ["Michelangelo"]),
    ("What is the fastest land animal?", ["cheetah"]),
    ("Which fruit has varieties called Cavendish and Gros Michel?", ["banana"]),
    ("What is the largest moon in our solar system?", ["Ganymede"]),
    ("Who composed 'F?r Elise'?", ["Beethoven"]),
    ("What is the chemical symbol for silver?", ["Ag"]),
    ("Which planet rotates on its side?", ["Uranus"]),
    ("What is the largest volcano in our solar system?", ["Olympus Mons"]),
    ("Who wrote 'The Communist Manifesto'?", ["Marx"]),
    ("What is the currency of Switzerland?", ["franc"]),
    ("Which element is liquid at room temperature?", ["mercury"]),
    ("What is the largest penguin species?", ["emperor penguin"]),
    ("Who discovered America?", ["Columbus"]),
    ("What is the most abundant gas in Earth's atmosphere?", ["nitrogen"]),
    ("Which country is shaped like a boot?", ["Italy"]),
    ("What is the largest snake species?", ["anaconda"]),
    ("Who developed the first polio vaccine?", ["Salk"]),
    ("What is the tallest waterfall in the world?", ["Angel Falls"]),
    ("Which animal has three hearts?", ["octopus"]),
    ("What is the capital of Egypt?", ["Cairo"]),
    ("Who created Sherlock Holmes?", ["Doyle"]),
    ("What is the largest land animal?", ["elephant"]),
    ("Which language is spoken in Brazil?", ["Portuguese"]),
    ("What is the hottest planet in our solar system?", ["Venus"]),
    ("Who was the first person in space?", ["Gagarin"]),
    ("What is the largest carnivorous marsupial?", ["Tasmanian devil"]),
    ("Which country has the most lakes?", ["Canada"]),
    ("What is the study of mushrooms called?", ["mycology"]),
    ("Who painted 'The Scream'?", ["Munch"]),
    ("What is the largest rodent?", ["capybara"]),
    ("Which country consumes the most chocolate?", ["Switzerland"]),
    ("What is the hardest mineral?", ["diamond"]),
    ("Who invented the light bulb?", ["Edison"]),
    ("What is the longest bone in the face?", ["mandible"]),
    ("Which planet has the fastest winds?", ["Neptune"]),
    ("What is the largest archipelago?", ["Indonesia"]),
    ("Who wrote 'The Odyssey'?", ["Homer"]),
    ("What is the national animal of Scotland?", ["unicorn"]),
    ("Which element has the lowest atomic number?", ["hydrogen"]),
    ("What is the capital of Iceland?", ["Reykjavik"]),
    ("Who discovered electricity?", ["Franklin"]),
    ("What is the largest big cat species?", ["tiger"]),
    ("Which country has the most time zones?", ["France"]),
    ("What is the world's most-spoken language?", ["Mandarin"]),
    ("Who proposed the heliocentric model?", ["Copernicus"]),
    ("Who is considered the father of modern physics?", ["Galileo"]),
	("What is the capital of Canada?", ["Ottawa"]),
    ("Who invented the World Wide Web?", ["Berners-Lee"]),
    ("Which gas is most abundant in Earth's atmosphere?", ["nitrogen"]),
    ("What is the largest country by land area?", ["Russia"]),
    ("Who wrote 'The Hitchhiker's Guide to the Galaxy'?", ["Adams"]),
    ("What is the primary language of Brazil?", ["Portuguese"]),
    ("Which organ produces insulin in the human body?", ["pancreas"]),
    ("What is the smallest U.S. state by area?", ["Rhode Island"]),
    ("Who was the first person to walk on the Moon?", ["Armstrong"]),
    ("What is the chemical symbol for iron?", ["Fe"]),
    ("Which planet has the shortest day?", ["Jupiter"]),
    ("What is the tallest building in the world?", ["Burj Khalifa"]),
    ("Who composed the 'Four Seasons' violin concertos?", ["Vivaldi"]),
    ("What is the main ingredient in hummus?", ["chickpeas"]),
    ("Which country is home to the kangaroo?", ["Australia"]),
    ("What is the freezing point of water at sea level?", ["0?C", "32?F"]),
    ("Who is known as the 'Queen of Pop'?", ["Madonna"]),
    ("What is the largest artery in the human body?", ["aorta"]),
    ("Which element is used in pencils?", ["graphite"]),
    ("What is the capital of Italy?", ["Rome"]),
    ("Who directed 'Jurassic Park'?", ["Spielberg"]),
    ("What is the name of the process plants use to make food?", ["photosynthesis"]),
    ("Which country is famous for the Eiffel Tower?", ["France"]),
    ("What is the largest rainforest in the world?", ["Amazon"]),
    ("Who discovered radioactivity?", ["Curie"]),
    ("What is the currency of South Africa?", ["rand"]),
    ("Which bird is a symbol of peace?", ["dove"]),
    ("What is the tallest tree species?", ["redwood"]),
    ("Who painted 'The Persistence of Memory'?", ["Dal?"]),
    ("What is the speed of sound in air?", ["343 m/s", "767 mph"]),
    ("Which planet has rings?", ["Saturn"]),
    ("What is the national animal of China?", ["dragon"]),
    ("Who wrote 'The Great Gatsby'?", ["Fitzgerald"]),
    ("What is the hardest bone in the human body?", ["mandible"]),
    ("Which country is known as the Land of the Midnight Sun?", ["Norway"]),
    ("What is the main component of natural gas?", ["methane"]),
    ("Who played Jack Sparrow in 'Pirates of the Caribbean'?", ["Depp"]),
    ("What is the largest fish in the ocean?", ["whale shark"]),
    ("Which city hosted the first modern Olympic Games?", ["Athens"]),
    ("What is the chemical formula for water?", ["H2O"]),
    ("Who is the Greek god of war?", ["Ares"]),
    ("What is the smallest U.S. state by population?", ["Wyoming"]),
    ("Which organ filters blood and produces bile?", ["liver"]),
    ("What is the capital of Mexico?", ["Mexico City"]),
    ("Who invented dynamite?", ["Nobel"]),
    ("What is the longest-running Broadway show?", ["Phantom"]),
    ("Which element has the atomic number 1?", ["hydrogen"]),
    ("What is the largest island in the Mediterranean Sea?", ["Sicily"]),
    ("Who wrote 'The Lord of the Rings'?", ["Tolkien"]),
    ("What is the largest muscle in the human body?", ["glutes"]),
    ("Which country is known for maple syrup?", ["Canada"]),
    ("What is the primary language of Egypt?", ["Arabic"]),
    ("Who painted 'The Birth of Venus'?", ["Botticelli"]),
    ("What is the coldest place on Earth?", ["Antarctica"]),
    ("Which planet has the most volcanoes?", ["Venus"]),
    ("What is the currency of India?", ["rupee"]),
    ("Who is the Roman goddess of love?", ["Venus"]),
    ("What is the largest lake in South America?", ["Titicaca"]),
    ("Who developed the first vaccine?", ["Jenner"]),
    ("What is the tallest statue in the world?", ["Statue of Unity"]),
    ("Which element is used in balloons to make them float?", ["helium"]),
    ("What is the capital of Thailand?", ["Bangkok"]),
    ("Who directed 'Titanic'?", ["Cameron"]),
    ("What is the main ingredient in traditional pesto?", ["basil"]),
    ("Which country is home to the Great Barrier Reef?", ["Australia"]),
    ("What is the largest moon of Saturn?", ["Titan"]),
    ("Who is known as the 'King of Rock and Roll'?", ["Presley"]),
    ("What is the fastest muscle in the human body?", ["eye muscles"]),
    ("Which planet is named after the Roman god of the sea?", ["Neptune"]),
    ("What is the national flower of Japan?", ["cherry blossom"]),
    ("Who invented the helicopter?", ["da Vinci"]),
    ("What is the most widely used programming language?", ["JavaScript"]),
    ("What is the smallest planet in our solar system?", ["Mercury"]),
    ("Which country is known as the 'Roof of the World'?", ["Tibet"]),
    ("Who wrote 'The Raven'?", ["Poe"]),
    ("What is the largest artery in the human body?", ["aorta"]),
    ("Which element is a poor conductor of heat?", ["wood"]),
    ("What is the capital of Kenya?", ["Nairobi"]),
    ("Who painted 'The Last Supper'?", ["da Vinci"]),
    ("What is the fastest muscle in the human body?", ["eye muscles"]),
    ("Which country has the longest coastline?", ["Canada"]),
    ("What is the main ingredient in sushi?", ["rice"]),
    ("Who is the Greek god of the underworld?", ["Hades"]),
    ("What is the largest city in Africa?", ["Lagos"]),
    ("Who discovered X-rays?", ["R?ntgen"]),
    ("What is the chemical symbol for potassium?", ["K"]),
    ("Which planet has a day longer than its year?", ["Venus"]),
    ("What is the national dish of Scotland?", ["haggis"]),
    ("Who wrote 'The Hobbit'?", ["Tolkien"]),
    ("What is the largest artery in the human body?", ["aorta"]),
    ("Which element is used in matches?", ["phosphorus"]),
    ("What is the capital of Argentina?", ["Buenos Aires"]),
    ("Who directed 'The Dark Knight'?", ["Nolan"]),
    ("What is the main ingredient in guacamole?", ["avocado"]),
    ("Which country is known for the Pyramids of Giza?", ["Egypt"]),
    ("What is the largest organ in the human body?", ["skin"]),
    ("Who is the Roman god of agriculture?", ["Saturn"]),
    ("What is the fastest muscle in the human body?", ["eye muscles"]),
    ("Which planet has the most extreme temperature variations?", ["Mercury"]),
    ("What is the national animal of Australia?", ["kangaroo"]),
]

def run_benchmark(temperature, run_number):
    correct = 0
    total_time = 0
    total_tokens = 0
    
    for question, keywords in trivia_benchmark:
        input_text = f"<|startoftext|>Question: {question}\nAnswer:"
        inputs = tokenizer(input_text, return_tensors='pt')
        
        start_time = time.time()
        outputs = model.generate(
            **inputs,
            max_length=256,
            temperature=temperature,
            repetition_penalty=1.2,
            do_sample=True
        )
        generation_time = time.time() - start_time
        
        full_text = tokenizer.decode(outputs[0])
        answer = full_text.split("Answer:")[1].strip() if "Answer:" in full_text else ""
        
        matched = any(keyword.lower() in answer.lower() for keyword in keywords)
        
        if matched:
            correct += 1
        total_time += generation_time
        total_tokens += outputs.shape[1] - inputs.input_ids.shape[1]
    
    accuracy = (correct / len(trivia_benchmark)) * 100
    speed = total_tokens / total_time if total_time > 0 else 0
    
    return {
        "temperature": temperature,
        "run": run_number,
        "accuracy": accuracy,
        "speed": speed,
        "total_time": total_time
    }

def benchmark_temperature_range():
    # Test temperatures from 0.1 to 1.0 in 0.1 increments
    temperatures = np.arange(0.1, 1.01, 0.1)
    results = []
    
    print(f"Starting benchmark for {len(temperatures)} temperatures with 5 runs each...")
    print(f"Total questions per run: {len(trivia_benchmark)}")
    print("=" * 70)
    
    for temp in temperatures:
        temp = round(temp, 1) 
        temp_results = []
        
        for run in range(1, 6):
            print(f"Running T={temp:.1f} - Run #{run}...")
            result = run_benchmark(temperature=temp, run_number=run)
            temp_results.append(result)
            results.append(result)
            print(f"  ? Accuracy: {result['accuracy']:.1f}% | Speed: {result['speed']:.1f} tokens/s")
        
        # Calculate averages for current temperature
        avg_acc = np.mean([r['accuracy'] for r in temp_results])
        avg_speed = np.mean([r['speed'] for r in temp_results])
        print(f"\nTemperature {temp:.1f} Summary:")
        print(f"  Average Accuracy: {avg_acc:.1f}%")
        print(f"  Average Speed:    {avg_speed:.1f} tokens/s")
        print("=" * 70)
    
    return results

def print_final_report(results):
    # Group results by temperature
    temp_groups = {}
    for r in results:
        t = r['temperature']
        if t not in temp_groups:
            temp_groups[t] = []
        temp_groups[t].append(r)
    
    print("\n\n" + "=" * 70)
    print("FINAL BENCHMARK REPORT")
    print("=" * 70)
    
    # Print results per temperature
    for temp, group in sorted(temp_groups.items()):
        accuracies = [r['accuracy'] for r in group]
        speeds = [r['speed'] for r in group]
        
        print(f"\nTemperature: {temp:.1f}")
        print("-" * 60)
        for i, r in enumerate(group, 1):
            print(f"Run {i}: {r['accuracy']:6.1f}% accuracy | {r['speed']:6.1f} tok/s")
        
        print(f"\nAverage:     {np.mean(accuracies):6.1f}% accuracy | {np.mean(speeds):6.1f} tok/s")
        print(f"Std Dev:     {np.std(accuracies):6.1f}%         | {np.std(speeds):6.1f} tok/s")
        print(f"Min/Max:     {min(accuracies):6.1f}%/{max(accuracies):.1f}%   | {min(speeds):6.1f}/{max(speeds):.1f} tok/s")
    
    # Find best performing temperature
    best_temp = max(temp_groups.items(), 
                   key=lambda x: np.mean([r['accuracy'] for r in x[1]]))
    print("\n" + "=" * 70)
    print(f"? OPTIMAL TEMPERATURE: {best_temp[0]:.1f} with {np.mean([r['accuracy'] for r in best_temp[1]]):.1f}% average accuracy")
    print("=" * 70)

if __name__ == "__main__":
    benchmark_results = benchmark_temperature_range()
    print_final_report(benchmark_results)