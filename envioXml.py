import logging
import os
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# flake8: noqa: E401, E501

logging.basicConfig(level=logging.INFO, filename="erro.log")

try:
    while True:
        diretorioCorrente = os.getcwd()
        arqConfig = open(rf"{diretorioCorrente}/configuracao.txt", "r", encoding="utf8")
        linhas = arqConfig.readlines()
        lista = []
        for linha in linhas:
            linha = linha.rstrip("\n")
            lista.append(linha)  # type: ignore

        host = "smtp.office365.com"
        port = "587"
        login = str(lista[0])  # type: ignore
        senha = str(lista[1])  # type: ignore

        tempo = int(lista[2]) * 3600  # type: ignore

        arqPastas = open(rf"{diretorioCorrente}/pastasEnvio.txt", "r", encoding="utf8")
        pastas = arqPastas.readlines()

        for pasta in pastas:
            arquivos = os.listdir(str(pasta.split("=")[0]))
            destinatario = str(pasta.split("=")[1])
            msg = MIMEMultipart()
            msg["To"] = destinatario
            msg["From"] = login
            msg["Subject"] = "Envio XML"

            body = MIMEText("Envio de XML", "html", "utf-8")
            msg.attach(body)
            for arquivo in arquivos:
                caminhoArquivo = os.path.join(str(pasta.split("=")[0]), arquivo)
                anexo = MIMEApplication(
                    open(caminhoArquivo, "rb").read(), _subtype="txt"
                )
                anexo.add_header("Content-Disposition", "anexo", filename=arquivo)
                msg.attach(anexo)
            server = smtplib.SMTP(host, port)  # type: ignore
            server.ehlo()
            server.starttls()
            server.login(login, senha)
            server.sendmail(msg["From"], msg["To"], msg.as_string())
            print("enviei para = " + destinatario)
            server.close()
            for arquivo in arquivos:
                caminhoArquivo = os.path.join(str(pasta.split("=")[0]), arquivo)
                os.remove(caminhoArquivo)
        print("Efetuarei os próximos envios em " + str(lista[2]) + " hora(s)")  # type: ignore
        time.sleep(tempo)
except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()  # type: ignore
    filename = exception_traceback.tb_frame.f_code.co_filename  # type: ignore
    line_number = exception_traceback.tb_lineno  # type: ignore

    logging.warning("Exception type: ", exception_type)  # type: ignore
    logging.warning("File name: ", filename)  # type: ignore
    logging.warning("Line number: ", line_number)  # type: ignore
    logging.warning("email de erro ", destinatario)  # type: ignore
