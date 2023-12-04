# send_email.py
# optmized by chapGPT

import logging
import os
import smtplib
import sys
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# flake8: noqa: E401, E501

logging.basicConfig(level=logging.INFO, filename="erro.log")


def send_email_with_attachments(host, port, login, senha, pasta, destinatario):  # type: ignore
    """
    Send an email with attachments.

    Args:
        host (str): SMTP server host.
        port (str): SMTP server port.
        login (str): Login username for SMTP server.
        senha (str): Login password for SMTP server.
        pasta (str): Folder path containing files to be attached.
        destinatario (str): Email address of the recipient.
    """
    try:
        arquivos = os.listdir(pasta)  # type: ignore
        msg = MIMEMultipart()
        msg["To"] = destinatario
        msg["From"] = login
        msg["Subject"] = "Envio XML"

        body = MIMEText("Envio de XML", "html", "utf-8")
        msg.attach(body)

        for arquivo in arquivos:  # type: ignore
            caminhoArquivo = os.path.join(pasta, arquivo)  # type: ignore
            with open(caminhoArquivo, "rb") as file:  # type: ignore
                anexo = MIMEApplication(file.read(), _subtype="txt")
                anexo.add_header("Content-Disposition", "attachment", filename=arquivo)  # type: ignore
                msg.attach(anexo)

        with smtplib.SMTP(host, port) as server:  # type: ignore
            server.ehlo()
            server.starttls()
            server.login(login, senha)  # type: ignore
            server.sendmail(msg["From"], msg["To"], msg.as_string())

        for arquivo in arquivos:  # type: ignore
            caminhoArquivo = os.path.join(pasta, arquivo)  # type: ignore
            os.remove(caminhoArquivo)  # type: ignore

        logging.info("Email sent to: " + destinatario)  # type: ignore
    except Exception as e:  # type: ignore
        exception_type, exception_object, exception_traceback = sys.exc_info()  # type: ignore
        filename = exception_traceback.tb_frame.f_code.co_filename  # type: ignore
        line_number = exception_traceback.tb_lineno  # type: ignore

        logging.warning("Exception type: " + str(exception_type))
        logging.warning("File name: " + filename)
        logging.warning("Line number: " + str(line_number))
        logging.warning("Error email: " + destinatario)  # type: ignore


def main():
    """
    Main function that sends emails with attachments from configured folders.
    """
    try:
        while True:
            diretorioCorrente = os.getcwd()
            config_path = os.path.join(diretorioCorrente, "configuracao.txt")
            arqConfig = open(config_path, "r", encoding="utf8")
            linhas = arqConfig.readlines()
            lista = [linha.rstrip("\n") for linha in linhas]

            host = "smtp.office365.com"
            port = 587
            login = str(lista[0])
            senha = str(lista[1])
            tempo = int(lista[2]) * 3600

            pastasEnvio_path = os.path.join(diretorioCorrente, "pastasEnvio.txt")
            arqPastas = open(pastasEnvio_path, "r", encoding="utf8")
            pastas = arqPastas.readlines()

            for pasta in pastas:
                pasta_path, destinatario = pasta.split("=")
                send_email_with_attachments(
                    host, port, login, senha, pasta_path.strip(), destinatario.strip()
                )

            print("Next sending will be in " + str(lista[2]) + " hour(s)")
            time.sleep(tempo)
    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:  # type: ignore
        exception_type, exception_object, exception_traceback = sys.exc_info()  # type: ignore
        filename = exception_traceback.tb_frame.f_code.co_filename  # type: ignore
        line_number = exception_traceback.tb_lineno  # type: ignore

        logging.warning("Exception type: " + str(exception_type))
        logging.warning("File name: " + filename)
        logging.warning("Line number: " + str(line_number))
        logging.warning("Error email: " + destinatario)  # type: ignore


if __name__ == "__main__":
    main()
