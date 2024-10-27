import psutil


def listar_procesos():
    print('PID        Nombre del Proceso    Uso de CPU (%)    Uso de Memoria')
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            pid = proc.info['pid']
            nombre = proc.info['name']
            cpu = proc.info['cpu_percent']
            memoria = proc.info['memory_info'].rss

            print(pid,"    ", nombre,"    ", cpu,"    ", memoria)

            # Mensaje para Notepad
            if nombre.lower() == 'notepad.exe':
                print("¡El Bloc de notas está en ejecución!")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


def finalizar_proceso(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(timeout=3)
        print("Proceso con PID ",pid," finalizado exitosamente.")
    except psutil.NoSuchProcess:
        print("No existe un proceso con el PID", pid)
    except psutil.AccessDenied:
        print("No tienes permisos para finalizar el proceso")
    except Exception as e:
        print("Ocurrió un error al intentar finalizar el proceso:", e)


def main():
    while True:
        print("Listado de procesos activos:")
        listar_procesos()

        try:
            pid_a_terminar = int(input("\nIngresa el PID del proceso que deseas terminar (0 para salir): "))
            if pid_a_terminar == 0:
                print("Saliendo del programa.")
                break
            finalizar_proceso(pid_a_terminar)
        except ValueError:
            print("Por favor, ingresa un número válido para el PID.")


if __name__ == "__main__":
    main()
