from gooey import Gooey, GooeyParser
#Fecha

@Gooey()
def main():
    parser = GooeyParser(description='Route monotoring')

    parser.add_argument(
        'Date select',
        help='Enter Date', widget='DateChooser')
        
    parser.add_argument(
    '--query', 
    help='Base search string'
)    
    args = parser.parse_args()
    print(args.query)
if __name__ == '__main__':
    main()
