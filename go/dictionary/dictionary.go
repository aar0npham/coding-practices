package dictionary

var (
	ErrNotFound         = DictionaryErr("Couldn't find the word in dict")
	ErrWordExists       = DictionaryErr("Cannot add word because it already exists")
	ErrWordDoesNotExist = DictionaryErr("Cannot update word because it does not exists")
)

type DictionaryErr string

func (e DictionaryErr) Error() string {
	return string(e)
}

var dictionary = map[string]string{}

// another way to do this is dictionary = make(map[string]string)

type Dictionary map[string]string

func (d Dictionary) Search(word string) (string, error) {
	def, ok := d[word]
	if !ok {
		return "", ErrNotFound
	}

	return def, nil
}

func (d Dictionary) Add(word, def string) error {
	_, err := d.Search(word)

	switch err {
	case ErrNotFound:
		d[word] = def
	case nil:
		return ErrWordExists
	default:
		return err
	}

	return nil
}

func (d Dictionary) Update(word, def string) error {
	_, err := d.Search(word)

	switch err {
	case ErrNotFound:
		return ErrWordDoesNotExist
	case nil:
		d[word] = def
	default:
		return err
	}

	return nil
}

func (d Dictionary) Delete(word string) {
	delete(d, word)
}
