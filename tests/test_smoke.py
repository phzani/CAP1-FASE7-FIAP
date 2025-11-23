import sys
import os
import importlib

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

modules_to_check = [
    'dashboard.views.fase1_view',
    'dashboard.views.fase2_view',
    'dashboard.views.fase3_view',
    'dashboard.views.fase4_view',
    'dashboard.views.fase5_view',
    'dashboard.views.fase6_view',
    'aws_service.messaging'
]

print("Verifying imports...")
failed = False
for module in modules_to_check:
    try:
        importlib.import_module(module)
        print(f"✅ {module} imported successfully")
    except Exception as e:
        print(f"❌ Failed to import {module}: {e}")
        failed = True

if failed:
    sys.exit(1)
else:
    print("All modules imported successfully!")
    sys.exit(0)
