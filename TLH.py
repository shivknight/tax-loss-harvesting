class TLH:

  vtsax = []
  lots = []
  def __init__(self):

    with open("VTSAX.csv") as f:
      self.vtsax = f.readlines()

    with open("costbasis.csv") as f:
      lots = f.readlines()

    # Remove header
    for l in lots[1:]:
      lot = l.split(',')
      self.lots.append(Lot(lot[0], lot[1]))

    for l in self.lots:
      print(l)

#    for l in self.vtsax:
#      vt_list = l.strip().split(',')
#      print(vt_list[0], vt_list[5])

  def SumLosses(self):
    print("stub")

class Lot:
  date_purchased = None
  value = 0

  def __init__(self, date, value):
    self.date_purchased = date
    self.value = value

  def __str__(self):
    return self.date_purchased + ": " + self.value

def main():
  tlh = TLH()

if __name__ == "__main__": main()
