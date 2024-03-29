import sys

app_dir = str(Path(__file__).resolve().parents[0])
sys.path.insert(0, app_dir)


from flaskapp import app as application