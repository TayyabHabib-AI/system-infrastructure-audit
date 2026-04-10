import psutil
import platform
import subprocess

def run_heavy_lab_audit():
    print("=== QUAID-E-AZAM SCHOOL: HEAVY LAB AUDIT ===")
    
    # 1. Check Processor
    print(f"CPU: {platform.processor()}")
    
    # 2. Check RAM
    ram_gb = round(psutil.virtual_memory().total / (1024**3), 2)
    print(f"RAM: {ram_gb} GB")
    
    # 3. Check for Dedicated GPU (NVIDIA Check)
    print("Checking for Dedicated GPU...")
    try:
        # This command checks the system for Video Controllers
        gpu_info = subprocess.check_output("wmic path win32_VideoController get name", shell=True).decode()
        if "NVIDIA" in gpu_info or "GTX" in gpu_info:
            print(f"GPU Detected: {gpu_info.splitlines()[2].strip()}")
            print("STATUS: Heavy Workload Ready.")
        else:
            print("GPU: Integrated Graphics Only.")
    except:
        print("GPU: Error detecting hardware.")
    
    print("============================================")

if __name__ == "__main__":
    run_heavy_lab_audit()