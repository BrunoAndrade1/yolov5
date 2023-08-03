import cv2
import torch
import numpy as np
import streamlit as st
from PIL import Image

#st.markdown("<h3 style='text-align: center; color: red;'>Objetos detectados na imagem:</h1>"+ ',' .join(translated_names), unsafe_allow_html=True)

st.markdown("<h3 style ='text-aling: center; color blue;'> Faça o upload de uma imagem e deixe-me identificar os objetos para você!:</h3>",unsafe_allow_html=True)

translation_dict = {
    "person": "pessoa", 
    "bicycle": "bicicleta", 
    "car": "carro",
    "motorbike": "moto",
    "aeroplane": "avião",
    "bus": "ônibus",
    "train": "trem",
    "truck": "caminhão",
    "boat": "barco",
    "traffic light": "semáforo",
    "fire hydrant": "hidrante",
    "stop sign": "placa de pare",
    "parking meter": "parquímetro",
    "bench": "banco",
    "bird": "pássaro",
    "cat": "gato",
    "dog": "cachorro",
    "horse": "cavalo",
    "sheep": "ovelha",
    "cow": "vaca",
    "elephant": "elefante",
    "bear": "urso",
    "zebra": "zebra",
    "giraffe": "girafa",
    "backpack": "mochila",
    "umbrella": "guarda-chuva",
    "handbag": "bolsa de mão",
    "tie": "gravata",
    "suitcase": "mala",
    "frisbee": "frisbee",
    "skis": "esquis",
    "snowboard": "prancha de snowboard",
    "sports ball": "bola esportiva",
    "kite": "pipa",
    "baseball bat": "taco de beisebol",
    "baseball glove": "luva de beisebol",
    "skateboard": "skate",
    "surfboard": "prancha de surf",
    "tennis racket": "raquete de tênis",
    "bottle": "garrafa",
    "wine glass": "copo de vinho",
    "cup": "xícara",
    "fork": "garfo",
    "knife": "faca",
    "spoon": "colher",
    "bowl": "tigela",
    "banana": "banana",
    "apple": "maçã",
    "sandwich": "sanduíche",
    "orange": "laranja",
    "broccoli": "brócolis",
    "carrot": "cenoura",
    "hot dog": "cachorro-quente",
    "pizza": "pizza",
    "donut": "rosquinha",
    "cake": "bolo",
    "chair": "cadeira",
    "sofa": "sofá",
    "pottedplant": "planta envasada",
    "bed": "cama",
    "diningtable": "mesa de jantar",
    "toilet": "vaso sanitário",
    "tvmonitor": "monitor de TV",
    "laptop": "laptop",
    "mouse": "mouse",
    "remote": "controle remoto",
    "keyboard": "teclado",
    "cell phone": "celular",
    "microwave": "micro-ondas",
    "oven": "forno",
    "toaster": "torradeira",
    "sink": "pia",
    "refrigerator": "geladeira",
    "book": "livro",
    "clock": "relógio",
    "vase": "vaso",
    "scissors": "tesoura",
    "teddy bear": "ursinho de pelúcia",
    "hair drier": "secador de cabelo",
    "toothbrush": "escova de dentes"
}


# Load the model
device = 'cpu'
if not hasattr(st, 'model'):
    st.model = torch.hub.load('ultralytics/yolov5', 'yolov5x', _verbose=False)

# Upload the image
uploaded_file = st.file_uploader("Faça upload de uma imagem", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = np.array(image)

    # Process objects
    results = st.model(img)

    # Draw the detections on the image
    object_list = []
    for *box, confidence, cls in results.xyxy[0]:
        # Add a bounding box to the image
        cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 2)

        # Add a label for the class name and confidence score
        cv2.putText(img, f'{results.names[int(cls)]} {confidence:.2f}', (int(box[0]), int(box[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

        # Add the detected object to the list
        object_list.append(results.names[int(cls)])

    # Convert the image colors from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the image
    st.image(img, use_column_width=True)
    translated_names = [translation_dict[name] for name in object_list if name in translation_dict]
    # Print the objects
    #st.write("Objetos detectados na imagem: ", translated_names)
    #st.markdown("**Objetos detectados na imagem:** " + ', '.join(translated_names))
    #st.markdown("<h3 style='text-align: center; color: red;'>Objetos detectados na imagem:</h1>"+ ',' .join(translated_names), unsafe_allow_html=True)
    #st.markdown("<h3 style='text-align: center; color: red;'>Objetos detectados na imagem: " + ', '.join(translated_names) + "</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: blue;'>Objetos detectados na imagem: </h3>" + 
                "<h3 style='text-align: center; color: red;'>" + ', '.join(translated_names) + "</h3>", unsafe_allow_html=True)


