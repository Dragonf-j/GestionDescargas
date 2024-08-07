import shutil
import os
from config import config
import logging
from Antivirus import Sistema_Antivirus


class move:
    carpeta_destino = ''
    carpeta_origen = ''
    contenido_File = ''
    def readDir(json):
        
        try:
            carpeta_origen = config.basicConfig.getPathOrigin(json) 
            contenido_File = os.listdir(carpeta_origen)
            ficheros = [f for f in contenido_File]
            carpeta_destino = config.basicConfig.getDestine(json)
            key = config.basicConfig.getAPIKey(json)
            for fic in ficheros:
                carpeta = ""
                carpeta= carpeta_origen + fic
                if Sistema_Antivirus.antiVirus.scanVirusTotal(fic,key) == 200:
                    #move.fileMove(carpeta, carpeta_destino)
                    print(Sistema_Antivirus.antiVirus.scanVirusTotal(fic))
                else:
                    #move.deleteFile(carpeta)
                    print(Sistema_Antivirus.antiVirus.scanVirusTotal(fic))    
            config.basicConfig.configLog(config.basicConfig.getLogName(json))
                
        except Exception as exp:
            logging.error(f"Se ha producido un error" +str(exp) )

    def fileMove(carpeta_origen, carpeta_destino):
        try:
            shutil.move(carpeta_origen, carpeta_destino)
            logging.info(f"Se mueven los ficheros de la carpeta de origen: " +carpeta_origen + " a la carpeta de destino: " +carpeta_destino+" correctamente")
        except Exception as exp:
            logging.error(f"Se ha producido un error al mover los ficheros de la carpeta de origen " +str(exp ))

    def deleteFile(carpeta):
        try:
            logging.info(f"Se procede a eliminar los datos ubicados en la " +carpeta)
            if os.path.isfile == True:
                os.remove(carpeta)
            else:
                shutil.rmtree(carpeta)
        except Exception as exp:
            logging.error(f"Se ha producido un error al eliminar los datos  " +str(exp ))




