# DS Library

## Information Extraction
We want to be able to extract information from PDF's. The text is the most
important thing, but it would be cool to have other information such as
chapters, pages, and possibly even images.

Obviously our first focus should be PDF's, then .epub, .mobi and maybe .djvu,
but another idea that came up was OCR for PDf's that don't have any text...
Is this something we might want to consider? How long do you think it would take
to processes these books? We'd have to come up with some sort of queue for that,
wouldn't we?

It seems to be there are two primary Python libraries for doing this:

- PDFMiner  
- Slate  

and then there's another service that incorporates all this stuff (tbh it looks
insanely bloated) called [ambar](https://ambar.cloud). I'm going to refrain from using it for now.

Anyways, after more research it looks like there's this Apache project called [Tika](https://tika.apache.org), which is supposedly the de-facto *standard* for text-extraction. I'm going to try it.

```bash
$ curl -X PUT --data-binary @resume.pdf http://localhost:9998/tika --header "Content-type: application/pdf"
```