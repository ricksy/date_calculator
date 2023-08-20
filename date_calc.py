import datetime
def main():
  d = datetime.date(2023, 7, 10)
  today = datetime.date.today()
  delta =  today - d
  juzu = int(delta.days) % 30
  print(f"it has been {delta} days since rebirth at {d} \n you should be reading Juzu {juzu}")

if __name__ == '__main__':
  main()
