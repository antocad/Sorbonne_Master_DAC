for $l in distinct-values(//bib/book/author/last),
    $f in distinct-values(//bib/book/author[last=$l]/first)
return
  <bp>
    {
      let $b := distinct-values(//bib/book[author/last = $l and author/first = $f]/title)
      return $b 
      if count($b) > 1
    }
  </bp>
  